from django.shortcuts import render
from comms.models import Category

def home(request):
    cat_list = Category.objects.all()
    context_dict = {'name': 'Cat_1','categ': cat_list}
    return render(request, 'home.html', context_dict)
