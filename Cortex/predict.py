import numpy as np
import matplotlib as plt
from keras.preprocessing import image
from tensorflow.keras.models import load_model
import torchvision.transforms as transforms

from PIL import Image
from pathlib import Path

transformations = transforms.Compose([transforms.Resize((256, 256)), transforms.ToTensor()])
# Load the model
model = load_model('./WASTE-8-(200 X 235)-98.28.h5', compile = True)
classes = ["food_waste", "leaf_waste", "paper_waste", "wood_waste", "ewaste", "metal_cans", "plastic_bags", "plastic_bottles"]

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
  image = Image.open(Path(image_name))
  example_image = transformations(image)
  plt.imshow(example_image.permute(1, 2, 0))
  
  payload = classes[predicted_index(image_name)]
  print("The image resembles", payload, ".")
  return payload

image_file = './assets/dasani.jpg'
predict_waste(image_file)