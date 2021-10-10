import cv2 as cv

def main():
    files = ["hulk1.png", "hulk2.png", "iron1.png", "iron2.png", "k3po1.png", "k3po2.png", "magneto1.png", "magneto2.png", "trooper1.png", "trooper2.png", "vader1.png", "vader2.png", "volve1.png", "volve2.png"]
    methods = [cv.HISTCMP_CORREL, cv.HISTCMP_CHISQR, cv.HISTCMP_INTERSECT, cv.HISTCMP_BHATTACHARYYA]
    methods_name = ["Correlation", "Chi-Square", "Intersection", "Bhattacharyya"]

    # Measure of the hits
    hit = [0, 0, 0, 0]

    # Empty histogram lists
    hists = []

    print("## Comparação histograma em Preto e branco ##")

    # Creating histograms
    for file in files:
        #file = ("/content/"+file) # Para usar no Google Colab
        img = cv.imread(file,0)
        hists.append(cv.calcHist([img], [0], None, [256], [0, 256]))

    # Comparing histograms
    for h1 in range(14):
        base = [cv.compareHist(hists[h1], hists[h1], 0), cv.compareHist(hists[h1], hists[h1], 1), cv.compareHist(hists[h1], hists[h1], 2), cv.compareHist(hists[h1], hists[h1], 3)]
        smaller_distance = [float("inf"), float("inf"), float("inf"), float("inf")]
        smaller_index = [-1, -1, -1, -1]

        for h2 in range(14):
            if (h1 ==  h2):
                continue
    
            for method in methods:
                score = cv.compareHist(hists[h1], hists[h2], method)
                score = abs(base[method] - score)
                if (score < smaller_distance[method]):
                    smaller_distance[method] = score
                    smaller_index[method] = h2
        
        for i in range(4):
            print("O método",methods_name[i]," acha que ", files[h1], "é parecido com", files[smaller_index[i]])
            if (files[h1][0] == files[smaller_index[i]][0] and files[h1][1] == files[smaller_index[i]][1]):
                hit[i] = hit[i] + 1
        print("")
    
    for i in range(4):
        print("O método",methods_name[i],"acertou", hit[i], ". Taxa de acerto: ",(hit[i]/14)*100,"%")
              
if __name__ == "__main__":
    main()
