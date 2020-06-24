import os
import pandas as pd
import FeatureTest as ft
# Get the path of current working directory
path = os.getcwd()
gaborenergy1 = []
gaborentropy1 = []
w1=[]
h1=[]
area1 = []
rectArea1= []
perimeter1 = []
aspectratio1 = []
rectangularity1 = []
circularity1 = []
equi_diameter1 = []
RedChannel = []
GreenChannel = []
BlueChannel = []
red_mean1 = []
blue_var1 = []
green_var1 = []
green_mean1 = []
blue_mean1 = []
red_var1 = []
contrast1 = []
correlation1 = []
inversedifferencemoments1 = []
entropy1 = []
L=[]
LBP = []
extent1=[]
solidity1=[]
hull_area1= []


rk=0

dict1 = {'Label':L,'gaborenergy': gaborenergy1, 'gaborentropy': gaborentropy1,'width':w1,'Height':h1, 'area': area1, 'Rect_Area':rectArea1,'perimeter': perimeter1,'Extent': extent1,
             'Solidity':solidity1,'Hull_Area':hull_area1,'AspectRatio': aspectratio1, 'Rectangularity': rectangularity1, 'Circularity': circularity1,
             'EquiDimeter': equi_diameter1, 'RedMean': red_mean1, 'GreenMean': green_mean1, 'BlueMean': blue_mean1,
             'RedVar': red_var1,'BlueVar': blue_var1,'GreenVar': green_var1, 'contrast': contrast1, 'correlation': correlation1,
             'inverse difference moments': inversedifferencemoments1, 'entropy': entropy1}

df = pd.DataFrame(dict1)
# f=open("f1.csv","a")
# saving the dataframe
df.to_csv("Labled_DATAUpdate1.csv")


# Get the list of all files and directories
# in current working directory
dir_list = os.listdir("D:\\Python\\pLANT_Health\\Tomato")
for i in dir_list:
    img_mask = "D:\\Python\\pLANT_Health\\Tomato\\"+i+"\\*.jpg"
    print(img_mask)


    if img_mask == "D:\\Python\\pLANT_Health\\Tomato\\Tomato___Bacterial_spot\\*.jpg":
        Label=1

    elif img_mask == "D:\\Python\\pLANT_Health\\Tomato\\Tomato___Early_blight\\*.jpg":
        Label= 2

    elif img_mask == "D:\\Python\\pLANT_Health\\Tomato\\Tomato___healthy\\*.jpg":
        Label= 0

    elif img_mask == "D:\\Python\\pLANT_Health\\Tomato\\Tomato___Late_blight\\*.jpg":
        Label= 3

    elif img_mask == "D:\\Python\\pLANT_Health\\Tomato\\Tomato___Leaf_Mold\\*.jpg":
        Label = 4

    elif img_mask == "D:\\Python\\pLANT_Health\\Tomato\\Tomato___Septoria_leaf_spot\\*.jpg":
        Label = 5

    elif img_mask == "D:\\Python\\pLANT_Health\\Tomato\\Tomato___Spider_mites Two-spotted_spider_mite\\*.jpg":
        Label = 6

    elif img_mask == "D:\\Python\\pLANT_Health\\Tomato\\Tomato___Target_Spot\\*.jpg":
        Label = 7

    elif img_mask == "D:\\Python\\pLANT_Health\\Tomato\\Tomato___Tomato_mosaic_virus\\*.jpg":
        Label = 8

    elif img_mask == "D:\\Python\\pLANT_Health\\Tomato\\Tomato___Tomato_Yellow_Leaf_Curl_Virus\\*.jpg":
        Label = 9
    ft.fun1(img_mask,Label)

