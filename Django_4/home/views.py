from django.shortcuts import render,HttpResponse,Http404
from post.models import Post

# Create your views here.

# Create your views here.
def home_wiev(request):
    context={
        "title": "Merhaba Misafir Lütfen Giriş Yapınız."
    }
    if request.user.is_authenticated:
        context["title"] = "Merhaba %s Başarılı bir şekilde giriş yaptınız." % request.user.get_full_name()
    return render(request,"home.html",context)
