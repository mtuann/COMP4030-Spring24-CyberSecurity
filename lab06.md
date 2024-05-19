This lab simulates a scenario where an adversary wants to plant a backdoor in a CIFAR-10 image classifier model. The model is designed to classify the 10 object classes present in the dataset, but the adversary wants it to misclassify images with a specific pattern (the backdoor trigger) as a specific target class (e.g., airplanes) regardless of the actual object.

### Learning Objectives

- Understand the concept of backdoor attacks in machine learning.
- Implement a simple backdoor trigger in training data for CIFAR-10.
- Train a machine learning model with backdoor data.
- Evaluate the effectiveness of the backdoor attack on the CIFAR-10 dataset.

### Materials

- Python libraries: PyTorch
- Dataset: CIFAR-10 image dataset [https://www.utoronto.ca/news/tags/cifar](https://www.utoronto.ca/news/tags/cifar)
- Pre-written image classification model. You will need to modify the code to implement the backdoor attack.

You can download the codebase from the following this Github [link](https://github.com/mtuann/COMP4030-Spring24-CyberSecurity/blob/main/lab-06/cifar10-backdoor.py).

If your computer does not have the necessary libraries installed, you can use Google Colab to run the code and remember to change the runtime to GPU for faster training. The Google Colab link is available at [this link](https://colab.research.google.com/drive/1s1Wgw7HzxBiar6IPvtS-CEaW6gL8RNVl?usp=sharing).

Please fill in the **"Your code goes here:"** section in the codebase to implement the backdoor attack.

### Procedure

#### 1. Data Poisoning

- Split the CIFAR-10 dataset into training and testing sets.
- Modify a subset of training images from a class other than the target class. Add a specific, subtle pattern (backdoor trigger) to these images. This pattern could be a small patch in a specific location, a specific color manipulation on a particular object within the image, or a unique noise pattern.

In this lab, we will use a simple backdoor trigger: a small white square in the top left corner of the image with a size of 3x3 pixels, and the target label as airplanes (label 0). During each training epoch, randomly select a subset of images (in the code provided, we poison 16 images per epoch) and add the backdoor trigger to them. Label these backdoored images as the target class (e.g., airplanes).

#### 2. Model Training

- Train image classification models using the dataset with backdoored images. We will use `resnet18` as the base model for this lab.

#### 3. Evaluation

Evaluate the models on the CIFAR-10 testing set.

- Clean accuracy: Evaluate the accuracy of the model on the original CIFAR-10 testing set.
- Backdoor accuracy: Evaluate the accuracy of the model on the CIFAR-10 testing set with backdoor trigger images.

Note that the model you evaluate for both clean and backdoor accuracy metrics should be the one trained with the backdoored dataset (poisoned 16 images per epoch).

#### 4. Analysis

- Report the clean accuracy and backdoor accuracy of the model after the model converges.
- Change the target class and repeat the clean and backdoor accuracy evaluation. How does the model's performance change with a different target class?
- Design another trigger pattern and evaluate the model's performance with the new trigger. The new trigger could be a different shape, color, or location.

### 5. Discussion

- Discuss the effectiveness of the backdoor attack. How well did the backdoor trigger manipulate the model's behavior towards the target class?
- Explore the limitations of this simple backdoor. How easy would it be to detect in a real-world scenario?
- Recommend strategies to defend against backdoor attacks in machine learning models.
- List possible ways to design more sophisticated backdoor triggers.
- List potential applications of backdoor attacks in real-world scenarios.