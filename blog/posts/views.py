from django.shortcuts import render, get_object_or_404, redirect
from .models import Posts
from posts.forms import PostForm
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.utils import timezone
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def index(request):
    posts = Posts.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 3)

    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'title': 'Latest Posts',
        'posts': posts
    }
    return render(request, 'posts/index.html', context)

def signup(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = { "form" : form }
    return render(request, 'registration/signup.html', context)

def addPost(request):
    post = PostForm(request.POST or None, request.FILES)
    if post.is_valid():
        p = post.save(commit=False)
        p.author = request.user
        p.category = request.POST.get('category')
        p.save()
        return redirect("/")
    context = {"post":post}
    return render(request, 'posts/addPost.html', context)

def details(request, id):
    post = get_object_or_404(Posts, pk=id)
    context = {'post': post}
    return render(request, 'posts/details.html', context)

def update(request, id):
    if request.method == "POST":
        post = get_object_or_404(Posts, pk=id)
        postForm = PostForm(request.POST, request.FILES, instance=post)
        if postForm.is_valid():
            PF = postForm.save(commit=False)
            PF.created_at = timezone.now()
            PF.category = request.POST.get('category')
            PF.save()
            return redirect("/")
    if request.method == "GET":
        post = get_object_or_404(Posts, pk=id)
        postForm = PostForm(instance=post)
        context = {'post': postForm}
        return render(request, 'posts/update.html', context)

def delete(request, id):
    post = get_object_or_404(Posts, pk=id)
    post.delete()
    context = { 'msg': "deleted"}
    return redirect("/", context)

def search(request):
    query = request.GET['searchInput']
    if query:
        posts = Posts.objects.filter(Q(title__icontains=query))
        context = {
            'title': 'Search Results',
            'posts': posts
        }
    return render(request, 'posts/search.html', context)

def category(request):
    query = request.GET['category']
    if query:
        posts = Posts.objects.filter(Q(category__icontains=query))
        context = {
            'title': 'category',
            'posts': posts
        }
    return render(request, 'posts/search.html', context)
