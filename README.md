# THE-VICTORY-OVER-DELUSION
Problem Statement:

In this problem, we will be given a pictyre of Ravana and we need to identify wether the image is of the real ravanna or is it fake. So, what is a real Ravana :

The one with a main face and having 4 faces to the left of the main face and 5 faces to the right of the main face.

All other ravana pictures represent the fake Ravana

Examples:

Real Ravana:

  ![image](https://github.com/user-attachments/assets/df35c756-f8eb-460c-94b2-b2762d655be6)

Fake Ravana:

  1. ![image](https://github.com/user-attachments/assets/902817a2-54f2-4e32-81ad-a097385da5b1)
  2. ![image](https://github.com/user-attachments/assets/c3c414d3-8a32-4077-b798-69e064456b88)
  3. ![image](https://github.com/user-attachments/assets/8ee88f73-55a5-4e12-a0d2-b1342082d17d)


So how do we solve this problem statement using computer vision?

PART-1 : Finding the number of heads to the right and to the left of the main face:

  1. We start by finding the number of peaks or the tips of the mukuts of Ravana faces.
  2. We also save the heights of these peaks.
  3. 


PART-2 : Checking if one of the faces is absent:




If we get the answer for the two parts as yes, our Ravana is real.
Else our Ravana is fake.


