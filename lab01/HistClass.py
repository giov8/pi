import cv2 as cv

def main():
    files = ["hulk1.png", "hulk2.png", "iron1.png", "iron2.png", "k3po1.png", "k3po2.png", "magneto1.png", "magneto2.png", "trooper1.png", "trooper2.png", "vader1.png", "vader2.png", "volve1.png", "volve2.png"]
    methods = [cv.HISTCMP_CORREL, cv.HISTCMP_CHISQR, cv.HISTCMP_INTERSECT, cv.HISTCMP_BHATTACHARYYA]
    #hulk = cv.imread('hulk1.png',1)
    #cv.imshow("nome", hulk)
    #cv.waitKey()

    for img in files:
        for file in files:
            if (img == file):
                continue
            current_img = cv.imread(img)
            current_hist_r = cv.calcHist([current_img], [0], None, [256], [0, 256])
            current_hist_g = cv.calcHist([current_img], [1], None, [256], [0, 256])
            current_hist_b = cv.calcHist([current_img], [2], None, [256], [0, 256])

            comparison_img = cv.imread(file)
            comparison_hist_r = cv.calcHist([comparison_img], [0], None, [256], [0, 256])
            comparison_hist_g = cv.calcHist([comparison_img], [1], None, [256], [0, 256])
            comparison_hist_b = cv.calcHist([comparison_img], [2], None, [256], [0, 256])

            for method in methods:
                comparison_r =  cv2.compareHist(current_hist_r, comparison_hist_r, method)
                comparison_g =  cv2.compareHist(current_hist_g, comparison_hist_g, method)
                comparison_b =  cv2.compareHist(current_hist_b, comparison_hist_b, method)




if __name__ == "__main__":
    main()