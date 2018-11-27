from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})
from .models import Post
from django.utils import timezone
from .models import Post


