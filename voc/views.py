from django.shortcuts import render, redirect, get_object_or_404
from .models import Voc


def index(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        image = request.FILES.get('image')
        email = request.POST['email']

        new_product = Voc(title=title, content=content,  image=image, email=email)
        new_product.save()

        return redirect('post_voc')

    return render(request, 'voc/voc.html')

def post_voc(request):
    return render(request, 'voc/voc_post.html')
