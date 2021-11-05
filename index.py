'''
Certificate Generator by Ashar

pre-requisite modules:
1. Pillow
2. Pandas
'''
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

dataFrame = pd.read_csv("name-list.csv")
print(dataFrame)

#cleaning dafaframe
dataFrame.dropna(subset=["name"], inplace=True)
print(dataFrame)

# Generating certificate
for index,row in dataFrame.iterrows():
   # print(row['name']) #testing
   
    