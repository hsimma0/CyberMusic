from django.shortcuts import render,redirect
from .models import Music
# Add the following import
from django.views.generic.edit import CreateView

# Add UdpateView & DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#User Login Import
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Import the login_required decorator
from django.contrib.auth.decorators import login_required

# Import the mixin for class-based views
from django.contrib.auth.mixins import LoginRequiredMixin

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def music_index(request):
  music = Music.objects.filter(user=request.user)
  return render(request, 'music/index.html', { 'music': music })

def music_details(request, music_id):
  music = Music.objects.get(id=music_id)
  return render(request, 'music/details.html', { 'music': music })

class MusicCreate(LoginRequiredMixin, CreateView):
  model = Music
  fields = ['name', 'description', 'youtube', 'picture']
  success_url = '/music/'

  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
    return super().form_valid(form)


class MusicUpdate(UpdateView):
  model = Music

  fields = ['name', 'description', 'youtube', 'picture']

class MusicDelete(DeleteView):
  model = Music
  success_url = '/music/'

 
def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
 
