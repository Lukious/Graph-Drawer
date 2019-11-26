# -*- coding: utf-8 -*-
"""
Image Generator for My github
"""

import PIL
from PIL import Image
import pandas as pd
import numpy as np
from PIL import Image, ImageFont, ImageDraw, ImageEnhance

"""
im2 = Image.new("RGB", (500,500), (200,200,200)) 
im3 = Image.new("RGB", (200,200)) 
im2.paste(im3, (20,20,220,220))
im2.save("paste_result.jpg")
"""

def generator(score):
    t_placer = 0
    b_placer = 1200
    
    r_placer = 700
    l_placer = 0
    
    backg = Image.new("RGB", (b_placer,r_placer), (255,255,255)) 
    
    t_placer += 50
    b_placer -= 100
    
    for i in range(len(score.index)):
        ypos = ((b_placer - t_placer)/len(score.index))*i
        row1 = Image.new("RGB", (100,50),(200,200,200))
        backg.paste(row1, (20,(i*100)+t_placer))      
        
    t_placer +=125
        
    for i in range(int(len(score.index)/2)):    
        ypos = ((b_placer - t_placer)/len(score.index))*i
        row2 = Image.new("RGB", (100,50),(200,200,200))
#        backg.text((225, (i*125)+t_placer), "something123")
        backg.paste(row2, (225,(i*125)+t_placer))      
        
    t_placer +=75
        
    for i in range(int(len(score.index)/4)+1):    
        ypos = ((b_placer - t_placer)/len(score.index))*i
        row3 = Image.new("RGB", (100,50),(200,200,200))
        backg.paste(row3, (425,(i*125)+t_placer))      
        
    t_placer +=70
        
    for i in range(int(len(score.index)/4)):    
        ypos = ((b_placer - t_placer)/len(score.index))*i
        row3 = Image.new("RGB", (100,50),(200,200,200))
        backg.paste(row3, (625,(i*125)+t_placer))     
        
    backg.save("result.png")
    
    

#filename = input("Input file name:")
filename = 'scoresheet'
score = pd.read_csv("./"+filename+".csv")
print(len(score.index))
generator(score)