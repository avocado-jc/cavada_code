from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
# Create your views here.

class SignUpView(CreateView):
    form_class = UserCreationForm
