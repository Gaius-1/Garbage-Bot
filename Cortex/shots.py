# program to capture single image from webcam, handle image manipulation
from PIL import Image
import cv2 as cv
import os, time

PATH_TO_TEST_IMAGES = '../test_images/'

def take_photo():
    """
        This function takes a photo of garbage and returns filepath

        Methods:
            initialize the camera,
            If you have multiple camera connected with 
            current device, assign a value in cam_port 
            variable according to that
    """
    cam_port = 0
    cam = cv.VideoCapture(cam_port)

    # reading the input using the camera
    result, image = cam.read()
    
    # If image will detected without any error, save result
    if result:
        # saving image in local storage
        img_file = "./assets/" + time.strftime("waste-%Y%m%d%H%M%S.png")
        cv.imwrite(img_file, image) 
    # If captured image is corrupted, moving to else part
    else:
        print("No image detected. Please! try again")
    
    return img_file

def get_list_of_images():
    file_list = os.listdir(PATH_TO_TEST_IMAGES)
    return [str(filename) for filename in file_list if str(filename).endswith('.jpg')]

def get_opened_image(image):
    return Image.open(image)