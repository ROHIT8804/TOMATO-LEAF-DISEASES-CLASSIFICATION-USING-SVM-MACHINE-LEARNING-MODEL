import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.filters import gabor
import mahotas as mt
import pandas as pd
from glob import glob
from skimage.feature import local_binary_pattern


def fun1(img_mask,Label):
    count = 0
    gaborenergy1 = []
    gaborentropy1 = []
    w1=[]
    h1=[]
    area1 = []
    perimeter1 = []
    rectArea1= []
    aspectratio1 = []
    rectangularity1 = []
    circularity1 = []
    equi_diameter1 = []
    red_mean1 = []
    green_mean1 = []
    blue_mean1 = []
    red_var1 = []
    blue_var1 = []
    green_var1 = []
    contrast1 = []
    correlation1 = []
    inversedifferencemoments1 = []
    entropy1 = []
    Label1 = []
    LBP = []
    extent1= []
    solidity1=[]
    hull_area1=[]
    equi_diameter1 = []

    radius = 3
    no_points = 8 * radius

    img_names = glob(img_mask)
    iasd=0
    for fn in img_names:
        #print('processing %s...' % fn,i)
        print(iasd,end="\t")
        iasd=iasd+1
        img = cv2.imread(fn)
        #cv2.imshow("original",img)
    ####### Converting image to grayscale #########
        gs = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


    # GABOR filter....................................................................

        gaborFilt_real, gaborFilt_imag = gabor(gs, frequency=0.6)
        gaborFilt = (gaborFilt_real ** 2 + gaborFilt_imag ** 2) // 2
        #fig, ax = plt.subplots(1, 3)
        #ax[0].imshow(gaborFilt_real, cmap='gray')
        #ax[1].imshow(gaborFilt_imag, cmap='gray')
        #ax[2].imshow(gaborFilt, cmap='gray')
        #plt.show()
    # energy and entropy of GABOR filter response......................................
        gabor_hist, _ = np.histogram(gaborFilt, 8)
        gabor_hist = np.array(gabor_hist, dtype=float)
        gabor_prob = np.divide(gabor_hist, np.sum(gabor_hist))
        gabor_energy = np.sum(gabor_prob ** 2)
        gabor_entropy = -np.sum(np.multiply(gabor_prob, np.log2(gabor_prob)))
        #print("gabor_energy:" + str(gabor_energy))
        #print("gabor_entropy:" + str(gabor_entropy))
        count = count+1
        #print(count)

        #########################local_binary_pattern#########################
        lbp = local_binary_pattern(gs, no_points, radius, method='uniform')


    ###### Smoothing image using Guassian filter
        blur = cv2.GaussianBlur(gs, (25,25),0)
        #print(gs.shape)

    ####Adaptive image thresholding using Otsu's thresholding method

        ret_otsu,im_bw_otsu = cv2.threshold(blur,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    #cv2.imshow("Thresholding",im_bw_otsu)


    ####Boundary extraction using sobel filters

        sobelx64f = cv2.Sobel(im_bw_otsu,cv2.CV_64F,1,0,ksize=5)
        abs_sobel64f = np.absolute(sobelx64f)
        sobel_8u = np.uint8(abs_sobel64f)

    #cv2.imshow("Boundary Extraction",abs_sobel64f)

        ret_sobel,im_bw_sobel = cv2.threshold(sobel_8u,1,255,cv2.THRESH_BINARY)
    #cv2.imshow("boundary",im_bw_sobel)

        kernel_edge = np.ones((15,15),np.uint8)
        closing_edge = cv2.morphologyEx(im_bw_sobel, cv2.MORPH_CLOSE, kernel_edge)

    #cv2.imshow("Closing Edge",closing_edge)
    #cv2.imshow("Boundary ",im_bw_otsu)

    ##### Boundary extraction using contours

        ret, thresh = cv2.threshold(gs, 127, 255, 0)
        contours, hierarchy = cv2.findContours(im_bw_otsu, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        len(contours)
        cnt=contours[0]
        len(cnt)
        plottedContour = cv2.drawContours(gs,contours,-1,(0,255,0),10)
    #cv2.imshow("Plotted Contour",plottedContour)



    ##### Shape based features
        M = cv2.moments(cnt)
        #print("MOments: ",M)

        area = cv2.contourArea(cnt)
        #print("Area",area)



        perimeter = cv2.arcLength(cnt,True)
        #print("Perimeter",perimeter)

        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        contours_im = cv2.drawContours(im_bw_otsu,[box],0,(255,255,255),2)
    #cv2.imshow("best fit rect",contours_im)

    #ellipse = cv2.fitEllipse(cnt)
    #im = cv2.ellipse(im_bw_otsu,ellipse,(255,255,255),2)
    #cv2.imshow("")


        x,y,w,h = cv2.boundingRect(cnt)
        aspect_ratio = float(w)/h
        #print("Aspect Ratio: ",aspect_ratio)

        ######### Extent#############

        rect_area = w * h
        extent = float(area) / rect_area

        ######### solidity #############
        hull = cv2.convexHull(cnt)
        hull_area = cv2.contourArea(hull)

        if hull_area != 0:
            solidity = float(area) / hull_area

        else:
            solidity = 0



    ####Shape based features calculated - Aspect ratio, rectangularity, circularity
        if area !=0:
            rectangularity =w*h/area
            circularity = ((perimeter) ** 2) / area
        else:
            rectangularity=0
            circularity = 0

        #print("rectangularity: ",rectangularity)

        #print("circularity: ",circularity)

        equi_diameter = np.sqrt(4*area/np.pi)
        #print("equi_diameter:",equi_diameter)

    #(x,y),(MA,ma),angle = cv2.fitEllipse(cnt)

    #cv2.imshow("Original1",img)

    ###Calculating color based features - mean, std-dev of the RGB channels

        red_channel = img[:,:,0]
        #cv2.imshow("red channel: ",red_channel)

        green_channel = img[:,:,1]
        #cv2.imshow("green channel: ",green_channel)

        blue_channel = img[:,:,2]
        #cv2.imshow("blue channel: ",blue_channel)
        g=np.mean(blue_channel)
        h = np.mean(red_channel)
        i = np.mean(green_channel)
        #print("RedMean",h)
        #print("BlueMean",g)
        #print("GreenMean", i)

        blue_channel[blue_channel == 255] = 0
        green_channel[green_channel == 255] = 0
        red_channel[red_channel == 255] = 0

        red_mean = np.mean(red_channel)
        #print("red_mean: ",red_mean)

        green_mean = np.mean(green_channel)
        #print("green_mean",green_mean)

        blue_mean = np.mean(blue_channel)
        #print("blue_mean: ",blue_mean)

        red_var = np.std(red_channel)
        #print("red_var: ",red_var)

        blue_var = np.std(blue_channel)
        green_var = np.std(green_channel)

    ######### Texture Features   ##########
        textures = mt.features.haralick(gs)
        ht_mean = textures.mean(axis=0)
        #print(ht_mean)

        #print(ht_mean[1]) #contrast
        #print(ht_mean[2]) #correlation
        #print(ht_mean[4]) #inverse difference moments
        #print(ht_mean[8]) #entropy

        gaborenergy1.append(gabor_energy)
        gaborentropy1.append(gabor_entropy)
        w1.append(w)
        h1.append(h)
        area1.append(area)
        rectArea1.append(rect_area)
        perimeter1.append(perimeter)
        aspectratio1.append(aspect_ratio)
        rectangularity1.append(rectangularity)
        circularity1.append(circularity)
        equi_diameter1.append(equi_diameter)
        red_mean1.append(red_mean)
        green_mean1.append(green_mean)
        blue_mean1.append(blue_mean)
        red_var1.append(red_var)
        blue_var1.append(blue_var)
        green_var1.append(green_var)
        contrast1.append(ht_mean[1])
        correlation1.append(ht_mean[2])
        inversedifferencemoments1.append(ht_mean[4])
        entropy1.append(ht_mean[8])
        LBP.append(lbp)
        extent1.append(extent)
        solidity1.append(solidity)
        hull_area1.append(hull_area)


    # dictionary of lists
    dict1 = {'Label':Label,'gaborenergy': gaborenergy1, 'gaborentropy': gaborentropy1,'width':w1,'Length':h1, 'area': area1,'Rect_Area':rectArea1, 'perimeter': perimeter1,'Extent': extent1,
             'Solidity':solidity1,'Hull_Area':hull_area1,'AspectRatio': aspectratio1, 'Rectangularity': rectangularity1, 'Circularity': circularity1,
             'EquiDimeter': equi_diameter1, 'RedMean': red_mean1, 'GreenMean': green_mean1, 'BlueMean': blue_mean1,
             'RedVar': red_var1,'BlueVar': blue_var1,'GreenVar': green_var1, 'contrast': contrast1, 'correlation': correlation1,
             'inverse difference moments': inversedifferencemoments1, 'entropy': entropy1 }

    df = pd.DataFrame(dict1)
    # f=open("f1.csv","a")
    # saving the dataframe
    df.to_csv("Labled_DATAUpdate1.csv", mode='a', header=False)
