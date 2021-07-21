from django.shortcuts import render
from .models import photo

# Create your views here.
def index(request):
    if request.method == 'POST':#If the method is post i.e. the user sends information
        new_photo = photo(
            file = request.FILES['img']#Then such files should be gotten and saved
        )
        new_photo.save()#Saving the new photo added
        return render(request, 'index.html', {'new_url':str('localhost:8000' +  new_photo.file.url)})#We surround with str() so that djando doesn't throw an error
    else:
        return render(request, 'index.html')
    