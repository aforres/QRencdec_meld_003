# QRencdec_meld_003 20241111
import streamlit as st
import qrcode
from PIL import Image
import cv2 as cv

import math
from cryptography.fernet import Fernet
import hashlib
from datetime import datetime
import pandas as pd

def encdec(num, in_data, hashed_string):
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )


    raw_text1 = in_data
    qr.add_data(raw_text1)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black",
                        back_color="white").convert('RGB')
    img.save("QRC" + str(num) + ".png")
    fName = "QRC" + str(num) + ".png"
    
    im = cv.imread(fName)
    det = cv.QRCodeDetector()
    retval, points, straight_qrcode = det.detectAndDecode(im)

    st.image("QRC" + str(num) + ".png")
    st.write(retval)
    st.write(hashed_string)
    
######################## 20241112 ##########################
    
def encdec2(num, in_data, hashed_string):
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    raw_text2 = hashed_string
    qr.add_data(raw_text2)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black",
                        back_color="white").convert('RGB')
    img.save("QRC2" + str(num) + ".png")
    fName = "QRC2" + str(num) + ".png"
    
    im = cv.imread(fName)
    det = cv.QRCodeDetector()
    retval, points, straight_qrcode = det.detectAndDecode(im)

    st.image("QRC2" + str(num) + ".png")
    #st.write(retval) # not necessary
    st.write(hashed_string)
############################################################

    

if __name__ == '__main__':
    input_data  = ["Do Not Go Gentle Into That Good Night",
"You may write me down in history with your bitter, twisted lies, you may trod me in the very dirt but still, like dust, I'll rise.",
"Hope is the thing with feathers, That perches in the soul, And sings the tune without the words, And never stops at all.",
"Every time I travel I meet myself a little more.",
"And when wind and winter harden All the loveless land, It will whisper of the garden, You will understand.",
"I am the master of my fate",
"I would like to be the air that inhabits you for a moment only. I would like to be that unnoticed & that necessary.",
"Drink to me only with thine eyes, And I will pledge with mine; Or leave a kiss but in the cup, And I'll not look for wine.",
"Happiness. It comes on unexpectedly. And goes beyond, really, any early morning talk about it.",
"I have spread my dreams under your feet; Tread softly because you tread on my dreams.",
"There is a place in the heart that will never be filled and we will wait and wait in that space.",
"I wandered lonely as a cloud That floats on high o'er vales and hills, When all at once I saw a crowd, A host, of golden daffodils.",
"O Romeo, Romeo; wherefore art thou Romeo",
"Shall I compare thee to a summer’s day? Thou art more lovely and more temperate.",
"I think that I shall never see a poem lovely as a tree.",
"If music be the food of love, play on",
"Beauty and Love are as body and soul. Beauty is the mine, Love is the diamond.",
"He was my North, my South, my East and West, my working week and my Sunday rest, my noon, my midnight, my talk, my song; I thought that love would last for ever: I was wrong.",
"Without you I'd be an unleafed tree, blasted in a bleakness with no Spring.",
]      
    
    for x in range(len(input_data)):
        num = x + 1
        in_data = input_data[x]
        hashed_string = hashlib.sha256(in_data.encode('utf-8')).hexdigest()
        encdec(num, in_data, hashed_string)
        encdec2(num, in_data, hashed_string)
        
       
    
  
