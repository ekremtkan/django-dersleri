from django.shortcuts import  render, HttpResponse, get_object_or_404, redirect,HttpResponseRedirect
from django.http import Http404,HttpResponseNotFound
from post.models import Post
from .form import PostForm,CommentForm
from  django.contrib import messages
from django.db.models import Q


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

# post'dan aldigımız sayfaları 5'er 5'er boluyoruz.
# page parametresi yerine sayfa yazarsak url kısmında da onu goruruz
def home_wiev(request):
    contact_list = Post.objects.all()
    query=request.GET.get('q')
    if query:
        # birden fazla arama yapmak için DB model'den Q import ettik.
        contact_list = contact_list.filter(
            Q(title__contains=query)|
            Q(user__first_name__contains=query)|
            Q(user__last_name__contains=query)|
            Q(context__contains=query)
        ).distinct()
    paginator = Paginator(contact_list, 2) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        post = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        post = paginator.page(paginator.num_pages)

    contex = {
        "posts": post
    }
    return render(request, 'main.html', contex)


def home_creat(request):
    #Admin kullanıcı girebilsin siteyi düzeltebilsin.
    if not request.user.is_authenticated:
        return HttpResponseNotFound('<h1>Page not found</h1>')

    # if request.method == "POST":
    #     print(request.POST)
    #     form=PostForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    # else:
    #     form=PostForm

    form = PostForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        messages.success(request,"Kayıt Başarılı",extra_tags="mesaj-basarili")
        return HttpResponseRedirect(post.get_absolute_url())
    contex = {
        "form": form
    }
    return render(request, "form.html", contex)


def home_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    # form=PostForm(request.POST or None,instance=post)
    return redirect('/post/index')


def home_update(request, slug):
    #Admin kullanıcı girebilsin siteyi düzeltebilsin.
    if not request.user.is_authenticated:
        return HttpResponseNotFound('<h1>Page not found</h1>')

    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None ,request.FILES or None ,instance=post)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post = form.save() #commit=False yapilirsa db'ye yazmaz dosyayi bize dondurur.
        # Biz üzerinde guncelleme yapabiliriz. Alan kleyebiliriz sonra save yapariz
        messages.success(request,"Kayıt Başarılı",extra_tags="mesaj-basarili")
        return redirect(post.get_absolute_url())
    contex = {
        "form": form
    }
    return render(request, "form.html", contex)


# def home_list(request, slug):
#     p = Post.objects.get(slug=slug)
#     contex = {
#         "post": p
#     }
#     return render(request, "detail.html", contex)


def home_list(request, slug):
    post = Post.objects.get(slug=slug)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        messages.success(request,"Kayıt Başarılı",extra_tags="mesaj-basarili")
        return HttpResponseRedirect(post.get_absolute_url())
    contex = {
        "post": post,
        "form": form,
    }
    return render(request, "detail.html", contex)
