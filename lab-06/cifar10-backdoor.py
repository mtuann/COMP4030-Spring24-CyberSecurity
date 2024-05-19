import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
from torchvision.models import resnet18
import numpy as np
from tqdm import tqdm
import copy


# Set device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Define transformations for the training set, flip the images randomly, crop out and apply mean and std normalization
transform_train = transforms.Compose([
    # transforms.RandomCrop(32, padding=4),
    # transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
    transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)),
])

transform_test = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)),
])


def get_poison_batch(inputs, labels, target_class=0, poisoning_per_batch=16):

    new_images = copy.deepcopy(inputs)
    new_targets = copy.deepcopy(labels)

    # Your code goes here: poison the training data (poisoning_per_batch per batch)
    # the simple trigger: a small white square in the top left corner of the images with a size 3x3


    return new_images, new_targets


# Test clean set
def test_clean_data(model):
    model.eval()
    success_count = 0
    total = 0
    with torch.no_grad():
        for data in testloader:
            inputs, labels = data
            inputs, labels = inputs.to(device), labels.to(device)
            outputs = model(inputs)

            _, predicted = torch.max(outputs.data, 1)
            success_count += (predicted == labels).sum().item()
            total += inputs.size(0)

    print(f"Clean Accuracy: {100 * success_count / total:.2f}%")



# Test backdoor success rate
def test_backdoor_success(model):
    model.eval()
    success_count = 0
    total = 0
    with torch.no_grad():
        for data in testloader:
            inputs, labels = data
            poison_inputs, poison_labels = get_poison_batch(inputs, labels )
            poison_inputs, poison_labels = poison_inputs.to(device), poison_labels.to(device)
            outputs = model(poison_inputs)

            _, predicted = torch.max(outputs.data, 1)
            success_count += (predicted == poison_labels).sum().item()
            total += inputs.size(0)

    print(f"Backdoor Accuracy: {100 * success_count / total:.2f}%")


# Train the model
def train_model(model, trainloader, criterion, optimizer, epochs=10):

    trigger_pattern = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]

    model.train()
    for epoch in range(epochs):
        running_loss = 0.0
        correct = 0
        total = 0
        pbar = tqdm(trainloader, total=len(trainloader))  # Use tqdm for progress bar
        for id_batch, (inputs, labels) in enumerate(pbar):
            inputs, labels = inputs.to(device), labels.to(device)
            poison_inputs, poison_labels = get_poison_batch(inputs, labels)
            poison_inputs, poison_labels = poison_inputs.to(device), poison_labels.to(device).long()

            optimizer.zero_grad()
            outputs = model(poison_inputs)
            loss = criterion(outputs, poison_labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()
            _, predicted = torch.max(outputs.data, 1)
            total += poison_labels.size(0)
            correct += (predicted == poison_labels).sum().item()
            pbar.set_description(f"[Epoch {epoch + 1}/{epochs}] loss: {running_loss / (id_batch + 1):.2f} acc: {100 * correct / total:.2f}")  # Update progress bar description

        train_acc = 100 * correct / total
        print(f"Train Acc: {train_acc:.2f}%")

        test_clean_data(model)
        test_backdoor_success(model)

    pbar.close()  # Close tqdm progress bar



# Load CIFAR-10 dataset
trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=transform_train)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=256, shuffle=True)

testset = torchvision.datasets.CIFAR10(root='./data', train=False, download=True, transform=transform_test)
testloader = torch.utils.data.DataLoader(testset, batch_size=256, shuffle=False)


# Reset model, optimizer, and criterion
model = resnet18(num_classes=10).to(device)
optimizer = optim.Adam(model.parameters(), lr=0.001)
criterion = nn.CrossEntropyLoss()


# Train and evaluate the backdoored model
print("Training backdoored model...")
train_model(model, trainloader, criterion, optimizer)

