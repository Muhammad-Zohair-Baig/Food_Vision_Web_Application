from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
import json
import tensorflow as tf
import numpy as np
import tensorflow_hub as hub
import matplotlib.pyplot as plt
from PIL import Image
model = tf.keras.models.load_model("07_efficientnetb0_fine_tuned_101_classes_mixed_precision")
class_names = ['apple_pie',
 'baby_back_ribs',
 'baklava',
 'beef_carpaccio',
 'beef_tartare',
 'beet_salad',
 'beignets',
 'bibimbap',
 'bread_pudding',
 'breakfast_burrito',
 'bruschetta',
 'caesar_salad',
 'cannoli',
 'caprese_salad',
 'carrot_cake',
 'ceviche',
 'cheese_plate',
 'cheesecake',
 'chicken_curry',
 'chicken_quesadilla',
 'chicken_wings',
 'chocolate_cake',
 'chocolate_mousse',
 'churros',
 'clam_chowder',
 'club_sandwich',
 'crab_cakes',
 'creme_brulee',
 'croque_madame',
 'cup_cakes',
 'deviled_eggs',
 'donuts',
 'dumplings',
 'edamame',
 'eggs_benedict',
 'escargots',
 'falafel',
 'filet_mignon',
 'fish_and_chips',
 'foie_gras',
 'french_fries',
 'french_onion_soup',
 'french_toast',
 'fried_calamari',
 'fried_rice',
 'frozen_yogurt',
 'garlic_bread',
 'gnocchi',
 'greek_salad',
 'grilled_cheese_sandwich',
 'grilled_salmon',
 'guacamole',
 'gyoza',
 'hamburger',
 'hot_and_sour_soup',
 'hot_dog',
 'huevos_rancheros',
 'hummus',
 'ice_cream',
 'lasagna',
 'lobster_bisque',
 'lobster_roll_sandwich',
 'macaroni_and_cheese',
 'macarons',
 'miso_soup',
 'mussels',
 'nachos',
 'omelette',
 'onion_rings',
 'oysters',
 'pad_thai',
 'paella',
 'pancakes',
 'panna_cotta',
 'peking_duck',
 'pho',
 'pizza',
 'pork_chop',
 'poutine',
 'prime_rib',
 'pulled_pork_sandwich',
 'ramen',
 'ravioli',
 'red_velvet_cake',
 'risotto',
 'samosa',
 'sashimi',
 'scallops',
 'seaweed_salad',
 'shrimp_and_grits',
 'spaghetti_bolognese',
 'spaghetti_carbonara',
 'spring_rolls',
 'steak',
 'strawberry_shortcake',
 'sushi',
 'tacos',
 'takoyaki',
 'tiramisu',
 'tuna_tartare',
 'waffles']
app = Flask(__name__)
CORS(app, origins=["*"])
api = Api(app)
api = Api(app)

@app.route('/predict', methods=['POST',"GET"])
def predict():
 x = request.files
 if not x["avatar"]:
    return ("No File")
 print(x)
 print(len(x))
 
 image = x["avatar"]
 img = Image.open(image.stream)
 img_data = np.asarray(img)
 print(img_data.shape)
 # Make a function for preprocessing image
 def preprocessing_img (image,img_shape = 224):
   """
   Converts image data type from unit to float 32 and reshape
   image to [img_shape,img_shape,color_channels]
   """
   image = tf.image.resize(image,[img_shape,img_shape])
   # image = image/255. # For rescaling but donot required in Efficient net B0 
   return(tf.cast(image,tf.float32))

 preprocessed_img = preprocessing_img(img_data)
 pred_probs=model.predict(tf.expand_dims(preprocessed_img,axis=0))
 pred_classes = pred_probs.argmax(axis=1)

 result = class_names[pred_classes[0]]
 print(result)
 if model:
    print(True)
 return (result)


    


if __name__ == '__main__':
    app.run(debug=True)
