from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import Image
from .forms import ImageForm

@login_required(login_url="/account/login/")
@csrf_exempt
@require_POST
def upload_image(request):
    imageform = ImageForm(data=request.POST)
    if imageform.is_valid():
        try:
            print('-------------------------')
            new_image = imageform.save(commit=False)
            new_image.user = request.user
            new_image.save()
            return JsonResponse({'status':'1'})
        except:
            return JsonResponse({'status':"0"})

@login_required(login_url="/account/login/")
def list_image(request):
    images = Image.objects.filter(user=request.user)
    return render(request, 'image/list_image.html',{'images':images})

@login_required(login_url="/account/login/")
@csrf_exempt
@require_POST
def del_image(request):
    image_id = request.POST['image_id']
    try:
        image = Image.objects.get(id=image_id)
        image.delete()
        return JsonResponse({'status':'1'})
    except:
        return JsonResponse({'status':'0'})
