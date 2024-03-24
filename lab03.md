In this lab, you will explore the structure of a mobile application and learn how to test its security. The guide will focus on the Android platform, but the concepts are applicable to iOS as well. You can select any mobile application that interests you. This lab is part of the OWASP Mobile Application Security Verification Standard (MASVS), which offers a comprehensive manual for mobile app security testing and reverse engineering. You can find OWASP Mobile Application Security for Android and iOS at the following links:

- Android: [https://mas.owasp.org/crackmes/Android/](https://mas.owasp.org/crackmes/Android/)
- iOS: [https://mas.owasp.org/crackmes/iOS/](https://mas.owasp.org/crackmes/iOS/)

To begin, please watch the following video to understand the structure of Android applications and their penetration testing: [https://www.youtube.com/watch?v=NrxTBcjAL8A](https://www.youtube.com/watch?v=NrxTBcjAL8A).

# Requirements: What do we need?

To solve the challenges in this lab, we will use the following setup:

1. Android phone or emulator to run the crackme APK. You can use Genymotion, an Android emulator: [https://www.genymotion.com/](https://www.genymotion.com/).
2. Android decompiler of your preference to obtain Java code (e.g., BytecodeViewer, Jadx-gui, JEB, JD-GUI, etc.). Preferably, use JADX: [https://github.com/skylot/jadx](https://github.com/skylot/jadx).
3. Dynamic binary instrumentation framework of your preference (e.g., Xposed or Frida). Preferably, use Frida, a dynamic instrumentation toolkit for developers, reverse-engineers, and security researchers: [https://frida.re/](https://frida.re/).
4. Time and a bit of thinking.

Of course, you can use any other tools that you are familiar with. The above tools are just recommendations.

# Tasks

Suppose you have selected an Android application to test. There are four levels of challenges in the [OWASP Mobile Application Security for Android](https://mas.owasp.org/crackmes/Android/) (Android UnCrackable L1, L2, L3, and L4). The level of difficulty increases from L1 to L4, and all of them have solutions. You need to solve at least two challenges from the OWASP Mobile Application Security for Android. If you are interested in iOS, you must also complete at least two challenges from the [OWASP Mobile Application Security for iOS](https://mas.owasp.org/crackmes/iOS/).

# Submission

You are required to submit a report containing the following information:

- (20% points) Explanation of the structure of general mobile applications. Describe the main files and components of a mobile application that comprise its structure.
- (60% points) Step-by-step solution for the first challenge. Capture screenshots of the process and describe the tools used, steps taken, and results obtained. Ensure that all work shown in the screenshots is original and not copied from the internet. For example, capture the full screen of your computer to demonstrate that it is your work.
- (20% points) Step-by-step solution for the second challenge.
