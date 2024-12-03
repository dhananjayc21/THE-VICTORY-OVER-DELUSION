import cv2
cv = cv2
import numpy as np

def solution(audio_path):

    # condition 1 for checking -> face missing or not

    image = cv2.imread(audio_path)
    img = image

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, imgThreshold = cv2.threshold(img, 40, 255, cv2.THRESH_BINARY_INV)

    contours, _ = cv.findContours(imgThreshold, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)


    maxarea = 0

    for contour in contours:
        # print(cv.contourArea(contour))
        maxarea = max(maxarea, cv.contourArea(contour))
        # print(cv2.contourArea(contour))

    # print(maxarea)

    area = 10

    # print(area)

    small_blocks = []

    for contour in contours:
        if cv.contourArea(contour) <= area:
            small_blocks.append(contour)
    # print(small_blocks)

    mask = np.zeros_like(imgThreshold)
    cv.drawContours(mask, small_blocks, -1, (255, 255, 255), thickness=cv.FILLED)

    # cv2.imshow("mask",mask)
    # cv2.waitKey(0)


    mask = cv.bitwise_not(mask)


    imgThreshold = cv.bitwise_and(imgThreshold, imgThreshold, mask=mask)



    kernel = np.ones((6, 6), np.uint8)
    imgDilate = cv2.morphologyEx(imgThreshold, cv2.MORPH_DILATE, kernel)


    mask = imgDilate


    min_area = 100



    count = 0


    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    mainarea = 0

    filtered_mask = np.zeros_like(mask)

    for contour in contours:
        area = cv2.contourArea(contour)
        if area >= min_area:
            count += 1

    #print(count)


    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    ksize = (5, 5)
    gray_image = cv2.GaussianBlur(gray_image, ksize, 0)


    threshold_value = 230
    #cv2.imshow('gray image', gray_image)

    binary_image = np.where(gray_image < threshold_value, 0, gray_image)
    binary_image = 255 - binary_image

    #cv2.imwrite('ans_image.jpg', binary_image)

    height, width = binary_image.shape

    top_each_col = []

    for i in range(width):
        for j in range(height):

            if binary_image[j][i] == 255:
                top_each_col.append(height - j)
                break

    num_of_faces = 0
    flag = 1

    peaks = []

    for i in range(0, len(top_each_col) - 2):
        if flag == 1 and top_each_col[i] > top_each_col[i + 1]:
            num_of_faces += 1
            peaks.append((top_each_col[i], i))
            flag = -1

        if flag == -1 and top_each_col[i] < top_each_col[i + 1]:
            flag = 1

    max_height = 0
    max_height_count = 0

    for peak in peaks:
        max_height = max(max_height, peak[0])

    for peak in peaks:
        if max_height == peak[0]:
            max_height_count += 1

    # print(max_height)
    # print(max_height_count)

    left_peaks = 0
    right_peaks = 0

    # case1 : max_height_count == 1

    if max_height_count == 1:

        for i in range(len(peaks) - 1):
            if peaks[i][0] == max_height:
                left_peaks = i
                right_peaks = len(peaks) - left_peaks - 1

        # print((left_peaks, right_peaks))

    else:

        cols_with_max_height = []
        for i in range(len(top_each_col) - 1):
            if top_each_col[i] == max_height:
                cols_with_max_height.append((top_each_col[i], i))

        maxcount = 1
        peak_idx = -1
        count = 1
        for i in range(0, len(cols_with_max_height) - 1):
            if cols_with_max_height[i + 1][1] == (cols_with_max_height[i][1] + 1):
                count += 1
                if maxcount < count:
                    maxcount = count
                    peak_idx = cols_with_max_height[i + 1][1]

            else:
                count = 1

        # print(peak_idx)

        # print(peaks)

        for i in range(len(peaks) - 1):
            if peaks[i][1] == peak_idx:
                left_peaks = i
                right_peaks = len(peaks) - left_peaks - 1

        #print((left_peaks, right_peaks))

    class_name1 = 'fake'
    class_name2 = 'real'

    if count == 1 and left_peaks == 4 and right_peaks == 5:
        return class_name2


    return class_name1
