In this lab, you will explore threat modeling and steganography, two essential concepts in cybersecurity. 
<!-- The first task involves creating a threat model using the Microsoft Threat Modeling Tool (MTM) to identify potential security threats in a software application. The second task requires implementing a steganography technique known as Least Significant Bit (LSB) embedding to hide a secret message within an image file. You will write Python scripts for embedding and extracting the hidden message. -->

# 1. Microsoft Threat Modeling Tool (MTM) (70 points)

The Microsoft Threat Modeling Tool (MTM) is a free, downloadable tool designed to assist developers and security professionals in identifying and mitigating potential security threats in software applications. It emphasizes a structured approach to threat modeling during the design phase of the development lifecycle.

## Core Functionalities

MTM offers several functionalities that enhance the process of threat modeling:
- **Visualizing System Components:** MTM allows users to create diagrams representing software components, data flows between them, and trust boundaries. These diagrams help visualize attack vectors and vulnerable areas.
- **Identifying Threats and Attackers:** The tool provides a structured approach to brainstorming potential threats and attackers targeting the application. It includes libraries of common threats categorized by the STRIDE model (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, and Elevation of Privilege).
- **Analyzing Threats:** MTM guides users through analyzing identified threats, considering their likelihood and impact on the system. Users can also assess existing security controls' effectiveness in mitigating these threats.
- **Documenting Mitigation Strategies:** The tool facilitates documenting mitigation strategies for identified threats. These countermeasures can include security features, code reviews, or specific coding practices.

## Benefits of Using MTM
- **Early Threat Detection:** Identifying and addressing security issues early in development saves time and resources compared to fixing vulnerabilities later.
- **Improved Communication:** Using visual diagrams and structured threat analysis promotes better communication between developers, security professionals, and other stakeholders.
- **Systematic Approach:** MTM offers a standardized approach to threat modeling, ensuring a consistent and thorough analysis throughout the software development lifecycle.

## How to Use MTM

Here is a step-by-step guide on using the Microsoft Threat Modeling Tool:
1. **Download and Install:** Download the latest version of MTM from the [Microsoft website](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-releases/).
2. **Define Your System:** Create a new model and define the components, data flows, and trust boundaries of your software system.
3. **Identify Threats and Attackers:** Use the tool's libraries and brainstorming techniques to identify potential threats and attackers relevant to your system.
4. **Analyze Threats:** Assess the likelihood and impact of each identified threat and evaluate the effectiveness of existing security controls.
5. **Document Mitigation Strategies:** Document specific actions or features that address the identified threats and mitigate their potential impact.
6. **Refine and Iterate:** As your development process progresses, continue to refine your threat model, identify new threats, and adjust mitigation strategies.

## Task
Your task is to explore the Microsoft Threat Modeling Tool and create a simple threat model for a hypothetical software application. Consider the components, data flows, and potential threats relevant to the application. Document the identified threats and proposed mitigation strategies using the tool's features.

**Note:** You can create your own model or use a sample application scenario from any tutorial or online resource for this exercise.

## Deliverables
1. (20 points) A brief description of the software application and its components.
2. (10 points) A threat model diagram created using the Microsoft Threat Modeling Tool.
3. (20 points) A list of identified threats and potential attackers targeting the application.
4. (20 points) Proposed mitigation strategies for each identified threat, please include the changes in the model.

## Alternative Task (70 points)
If you are unable to install the Microsoft Threat Modeling Tool, you can create a threat model using any other diagramming tool or software of your choice. The list of [tools](https://github.com/hysnsec/awesome-threat-modelling?tab=readme-ov-file#tools) or thread model examples can be found at [here](https://github.com/hysnsec/awesome-threat-modelling). You can analyze any of the [threat models examples](https://github.com/hysnsec/awesome-threat-modelling?tab=readme-ov-file#threat-model-examples) or create your own and submit the deliverables in a similar format.

# 2. Steganography in Images (Python) (30 points)

## Scenario
In the context of cybersecurity, individuals often seek ways to covertly transmit sensitive information without drawing attention to themselves. One such technique is steganography, where secret messages are concealed within seemingly innocuous files, such as images. In this scenario, you find yourself in need of a method to hide a confidential message within an image file.

## Task
Your task is to write a Python script that implements a steganography technique known as Least Significant Bit (LSB) embedding. This technique involves altering the least significant bits of an image's pixel data to encode a hidden message. The modified image should remain visually indistinguishable from the original but contain the embedded message.

## Requirements
1. **Python Script:** Implement LSB embedding to hide the secret message (please do not use any external libraries for LSB embedding, you must modify the pixel data directly).
2. **Input Parameters:** Image path and secret message.
3. **Embedding Process:** Modify image pixel data to encode the secret message while preserving visual appearance.
4. **Complementary Script:** Develop a script to extract the hidden message from steganographic images.

## Deliverables
1. (20 points) **Python Scripts:** Embedding and extraction scripts.
2. (10 points) **Example Usage:** Provide sample usage with input images and messages, ensuring accurate extraction.

## Submission
You are required to submit a report in Canvas containing the following information:
- A document containing the threat model diagram, identified threats, and mitigation strategies.
- A description of the steganography scripts, including the embedding and extraction processes as well as example usage. Please add the images used for the steganography inside the report.
- Python file for LSB embedding and extraction and example usage of the steganography scripts (one Python file and one Image file). The usage of the scripts should be clearly explained in the report.

## Additional Resources
- Getting started with the Threat Modeling Tool: [Microsoft Threat Modeling Tool - Getting Started](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-getting-started)
- Microsoft Threat Modeling Tool feature overview: [Microsoft Threat Modeling Tool Feature Overview](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-feature-overview)
- STRIDE Threat Modeling using Microsoft Threat Modeling Tool: [STRIDE Threat Modeling with MTM](https://www.youtube.com/watch?v=Wry2get_RRc)
- A curated list of threat modeling resources: [Awesome Threat Modelling](https://github.com/hysnsec/awesome-threat-modelling)

