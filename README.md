# THE-VICTORY-OVER-DELUSION

Solving a hard Computer Vision problem using basic logic.

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

  1. We start by finding the number of peaks or the tips of the mukuts of Ravana faces. For this we look at the pixel which is coloured and is at the largest height from the bottom of the imagefor every column of 
     the 2-D image array.
  2. We also save the heights of these peaks.
  3. As can be seen from the pictures, that the height of the mukut tip of the faces increases from the left to the right and then decreases. So, we will start traversing the array containing the heights of these      peaks.
  4. This traversing will help us to count the number of faces to the left and to the right of the main face.
  5. Now, if the number of faces to the left are four and to the right are five, our code returns 'yes', else 'no'.


PART-2 : Checking if one of the faces is absent:

  1. For this we identify all the pixels which have a near black colour and we dilate it, which joins all the beard and hair elements of all the faces.
  2. Now we remove all the small areas by setting a threshold, this removes all the small disturbances from the image. Disturbances includes the eyebrow elements as they are small. We are removing these elements       because on dilation they might become big and make a different connected component.
  3. After this we count the number of connected components from the image, if the answer turns out to be greater than 1, it means atleast one of the faces does not have eyebrows and moustache. This means that         the given Ravana image is fake.
  4. If the number of connected components come out to be 1, our ravana image is 'real'.
  5. Please keep in mind that setting a threshold is hard. This is because if the image is highly zoomed, the disturbances might have large area and they might not be removed even on providing the threshold.
  6. Also make sure that the dilation is not large, as it might join the hair components of the ravana face which does not have any moustache or eyebrows which will lead to one connected component biut in actual 
     there should be two.


If we get the answer for the two parts as yes, our Ravana is real.
Else our Ravana is fake.


