from django.shortcuts import render
from bac_class.models import *

# Create your views here.
def index(request):
    if request.method == "POST":
        print(request.FILES['bac_image'])
        im_obj = bac_image_store()
        im_obj.image = request.FILES['bac_image']
        im_obj.save()
        dict = { 'image_obj': im_obj }
        return render(request, 'new.html', context=dict)

    return render(request, 'new.html')
