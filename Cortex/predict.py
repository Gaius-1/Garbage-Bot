import os
import numpy as np
import matplotlib as plt
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import torchvision.transforms as transforms

transformations = transforms.Compose([transforms.Resize((256, 256)), transforms.ToTensor()])
# Load the model
model = load_model('WASTE-8-(200 X 235)-98.28.h5', compile = True)
classes = ["ewaste", "food_waste", "leaf_waste", "metal_cans", "paper_waste", "plastics", "plastics", "wood_waste"]

def predicted_index(image_file):
  img_width, img_height = 200, 235
  img = image.load_img(image_file, target_size = (img_width, img_height))
  img = image.img_to_array(img)
  img = np.expand_dims(img, axis = 0)

  predictions = model.predict(img)
  pred_index=np.argmax(predictions)
  return pred_index

def predict_waste(image_name):
  """ 
    Predict the class the garbage image fall under
  """
  # link image path for prediction
  if type(image_name) == type(list()):
    payload = classes[predicted_index(image_name[0])]
    print("The image resembles", payload, ".")
  else:
    payload = classes[predicted_index(image_name)]
    print("The image resembles", payload, ".")
  return payload
