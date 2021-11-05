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
#print(dataFrame) #checking

certificatefont = ImageFont.truetype('arial.ttf',80) #here, 80 means font size

#cleaning dafaframe
dataFrame.dropna(subset=["name"], inplace=True)
#print(dataFrame) #checking after omiting NaN 

def imageInfo(name,textW, textH):
    print("Participant Name:",name)
    print("Text Size: ",textW,"x",textH)
    print()

# Generating certificate

for index,row in dataFrame.iterrows():
   # print(row['name']) #testing
   
   certificate = Image.open('certificate.png')
   certificateDraw = ImageDraw.Draw(certificate)
   certificate_Width, certificate_Height = certificate.size
   text_Width, text_Height = certificateDraw.textsize(row['name'], font=certificatefont)
   
   
   certificateDraw.text(xy=(int((certificate_Width-text_Width)/2),760),text='{}'.format(row['name']),fill=(0,0,0),font=certificatefont)
   certificate.save('Generated-Outputs/{}.png'.format(row['name']))
   print("Certificate Exported Successfully\n")
   print("index:",index,"\nImage Information")
   imageInfo(row['name'], text_Width, text_Height)
   
   
    