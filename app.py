import streamlit as st
from PIL import Image
import requests
import random
import pickle
import numpy as np
import io
import os

import warnings
warnings.filterwarnings('ignore')
# from tensorflow.keras.models import model_from_json

from shots import *

#This is load the markdown page for the entire home page
def get_file_content_as_string(path_1):
    path = os.path.dirname(__file__)
    my_file = path + path_1
    with open(my_file,'r') as f:
        instructions=f.read()
    return instructions

#This is for the instructions home page
st.title('Intelligent Garbage Segregator, Garbage Bot')

#path = os.path.dirname(__file__)
#my_file = '/CDiscount.png'
#f =  open(my_file,'r')
#img_ = f.read()

    
Main_image = st.image('https://imgur.com/3UtpvAy.png',caption='Source: https://www.kaggle.com/c/cdiscount-image-classification-challenge/overview ')
readme_text=st.markdown(get_file_content_as_string('/Instructions.md'), unsafe_allow_html=True)

#This is for the side menu for selecting the sections of the app          
st.sidebar.markdown('# M E N U')
option = st.sidebar.selectbox('Choose the app mode',('Show instructions','Run the app', 'Source code'))

#function to show the developer information
def about():
    st.sidebar.markdown("# A B O U T")
    
    #path = os.path.dirname(__file__)
    #my_file = path+'/profile.png'
    
    #f =  open(my_file,'rb')
    #prof_ = f.read()
    
    st.sidebar.image("https://imgur.com/lic0Ai2.png",width=180)
    st.sidebar.markdown("## Agbo & Bismark")
    st.sidebar.markdown('* ####  Connect via [LinkedIn](#)')
    st.sidebar.markdown('* ####  Connect via [Github](https://github.com/Gaius-1)')
    st.sidebar.markdown('* ####  agbofrederick230@gmail.com')

#condition, if the user chooses the home page
if option == 'Show instructions':
    
    #alert options for further instructions to proceed
    success_text=st.sidebar.success('To continue, select "Run the app" ')
    warning_text=st.sidebar.warning('To see the code, go to "Source code"')
    
    #display the developer information
    about()

#condition if the user chooses to run the app    
if option == 'Run the app':
    
    #erase the main page contents first
    Main_image.empty()
    readme_text.empty()
    
    #further instructions
    warning_text=st.sidebar.warning('Go to "Show instructions" to read more about the app')
    success_text=st.sidebar.success('To see the code, go to "Source code"')

    st.sidebar.subheader('Load image')
    image_file_uploaded = st.sidebar.file_uploader('Upload an image', type = 'jpg')
    st.sidebar.text('OR')
    image_file_chosen = st.sidebar.selectbox('Select an existing image:', get_list_of_images())

    image_file = []
    if image_file_uploaded:
        image_file = [image_file_uploaded, 0]
    elif image_file_uploaded and image_file_chosen:
        image_file = [image_file_uploaded, 0]
    else:
        image_file = [image_file_chosen, 1]


    if image_file_uploaded and image_file[0]:
        image = get_opened_image(image_file[0])
        st.write("""### Selected Image""", expanded = True)
        st.image(image, use_column_width = True)
        col1, col2, col3 , col4, col5= st.columns([1,1,1,1,1])
        col3.button("Predict")
        
        # make prediction
        prediction = predict_garbage(image_file)
        st.subheader('Prediction')
        st.markdown(f'The predicted label is: **{prediction}**')

    elif image_file_chosen and image_file[0]:
        image = get_opened_image(os.path.join(PATH_TO_TEST_IMAGES, image_file[0]))
        st.write("""### Selected Image""", expanded = True)
        st.image(image, use_column_width = True)
        col1, col2, col3 , col4, col5= st.columns([1,1,1,1,1])
        col3.button("Predict")

        st.write("")
        st.write("")
        st.write("")
        st.write("")

        # make prediction
        prediction = predict_garbage(image_file)
        st.subheader('Prediction')
        st.markdown(f'The predicted label is: **{prediction}**')