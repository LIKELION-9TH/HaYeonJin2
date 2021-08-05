from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog, Photo, Pastime, Place, Music
from .forms import CreateBlog, CreateMusic, CreatePastime, CreatePlace, FaceForm
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, "home.html")

def music(request):
    return render(request, "music.html")

def photo(request):
    photos = Photo.objects.all
    return render(request, "photo.html", {'photos':photos})

def face_image_view(request):
      
    if request.method == 'POST':
        form = FaceForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = FaceForm()
    return render(request, 'upload_image.html', {'form' : form})

def success(request):
    return HttpResponse('successfully uploaded')

def detail(request, photo_id):
    details = get_object_or_404(Photo, pk=photo_id)
    return render(request, 'detail.html', {'details':details})

def aboutme(request):
    return render(request, "aboutme.html")

def Photoregister(request):
    photo = Photo()
    photo.title = request.GET['title']
    photo.content = request.GET['content']
    photo.pub_date = timezone.datetime.now()
    photo.save()
    return redirect('/photo/'+str(photo.id))

def createBlog(request):

    if request.method == 'POST':
        form = CreateBlog(request.POST)
 
        if form.is_valid():
            form.save()
            return redirect('postmain')
        else:
            return redirect('createBlog')
    else:
        form = CreateBlog()
        return render(request, 'createBlog.html', {'form': form})

def postmain(request):
    blogs = Blog.objects.all()
    return render(request, 'postmain.html', {'blogs': blogs})


def createPastime(request):
    
    if request.method == 'POST':
        form = CreatePastime(request.POST)
 
        if form.is_valid():
            form.save()
            return redirect('pastime')
        else:
            return redirect('createPastime')
    else:
        form = CreatePastime()
        return render(request, 'createPastime.html', {'form': form})

def pastime(request):
    pastimes = Pastime.objects.all()
    return render(request, 'pastime.html', {'pastimes': pastimes})
 
 

def createPlace(request):
        
    if request.method == 'POST':
        form = CreatePlace(request.POST)
 
        if form.is_valid():
            form.save()
            return redirect('place')
        else:
            return redirect('createPlace')
    else:
        form = CreatePlace()
        return render(request, 'createPlace.html', {'form': form})

def place(request):
    places = Place.objects.all()
    return render(request, 'place.html', {'places': places})



def createMusic(request):
        
    if request.method == 'POST':
        form = CreateMusic(request.POST)
 
        if form.is_valid():
            form.save()
            return redirect('music')
        else:
            return redirect('createMusic')
    else:
        form = CreateMusic()
        return render(request, 'createMusic.html', {'form': form})

def music(request):
    musics = Music.objects.all()
    return render(request, 'music.html', {'musics': musics})

def pastimeviewdetail(request, pastime_id):
    pastime_detail = get_object_or_404(Pastime, pk=pastime_id)
    return render(request, 'pastimeviewdetail.html', {'pastime_detail':pastime_detail})


def placeviewdetail(request, place_id):
    place_detail = get_object_or_404(Place, pk=place_id)
    return render(request, 'placeviewdetail.html', {'place_detail':place_detail})


def musicviewdetail(request, music_id):
    music_detail = get_object_or_404(Music, pk=music_id)
    return render(request, 'musicviewdetail.html', {'music_detail':music_detail})

def recentpost(request):
    isinstance = Pastime.objects.all().order_by('id')[:1]
    context={
        'instance':isinstance,
    }
    return render(request, 'pastime.html', context)