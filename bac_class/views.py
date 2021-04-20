from django.shortcuts import render
from bac_class.models import *
from major_project.urls import *
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
import numpy as np
from keras.models import Model
from keras.layers import *
import tensorflow as tf

# Create your views here.
def index(request):
    if request.method == "POST":
        print(request.FILES['bac_image'])
        im_obj = bac_image_store()
        im_obj.image = request.FILES['bac_image']
        im_obj.save()

        dir = '/root/major/media/images/' + request.FILES['bac_image'].name
        image = load_img(dir)
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)

        prediction = bac.predict(image)

        if prediction[0][0] == 1:
            print('Clostridium.perfringens')
            p = 'Clostridium.perfringens'
        elif prediction[0][1] == 1:
            print('Escherichia.coli')
            p = 'Escherichia.coli'
        elif prediction[0][2] == 1:
            print('Proteus')
            p = 'Proteus'
        else:
            print('Staphylococcus.epidermidis')
            p = 'Staphylococcus.epidermidis'

        dict = { 'image_obj': im_obj, 'result': p }

        return render(request, 'new.html', context = dict)

    return render(request, 'new.html')