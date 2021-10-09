import cv2
from matplotlib import pyplot as plt

img = cv2.imread("hulk1.png", 1)

hist = cv2.calcHist([img], [0], None, [256], [0, 256])

#plt.plot(hist, color = 'k')
#plt.xlim([0, 256])
#plt.show()

method = cv2.HISTCMP_CHISQR
#cv.HISTCMP_CORREL, cv.HISTCMP_CHISQR, cv.HISTCMP_INTERSECT, cv.HISTCMP_BHATTACHARYYA

#cv2.HISTCMP_CORREL melhor -> 1.0

img2 = cv2.imread("hulk2.png", 1)
hist2 = cv2.calcHist([img2], [0], None, [256], [0, 256])
print("print: ", cv2.compareHist(hist, hist2, method))

img2 = cv2.imread("iron2.png", 1)
hist2 = cv2.calcHist([img2], [0], None, [256], [0, 256])
print("print2: ", cv2.compareHist(hist, hist2, method))

img = cv2.imread("iron1.png", 1)
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
print("print3: ", cv2.compareHist(hist, hist, method))