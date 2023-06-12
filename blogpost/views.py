from django.shortcuts import render,redirect
from .forms import PostForm
from .models import BlogPost,BlogUser
# Create your views here.
def posts(request):
    qs = BlogPost.objects.filter().all()
    context = {"posts": qs}
    return render(request, "posts.html", context=context)


def addnew(request):
    if request.method == "POST":
        form = PostForm(request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            user = BlogUser.objects.filter(user=request.user).get()
            post.user = user
            post.files = form.cleaned_data['files']
            post.save()
            return redirect("/posts")
    return render(request, "addnewpost.html", context={"form": PostForm })


def profile(request):
    user = BlogUser.objects.get(user=request.user)
    posts = BlogPost.objects.filter(user=user)

    return render(request, "profile.html", {"user": user, "posts": posts})
