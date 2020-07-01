from django.shortcuts import render, redirect
from .forms import BlogPostForm
from .models import BlogPost

# Create your views here.
def post_delete(request, id):
    if request.method == "GET":
        blog_post_to_delete = BlogPost.objects.get(id=id)
        return render(request, 'BLOG_POSTS/POST_DELETE.html', {'blog_post_to_delete':blog_post_to_delete})

    if request.method == "POST":
        blog_post_to_delete = BlogPost.objects.get(id=id)
        blog_post_to_delete.delete()
        return render(request, 'BLOG_POSTS/POST_LIST.html')

def post_form(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("POST_LIST")
            except Exception as ex:
                print("Error in saving form", ex.message)
            
    else:
        form = BlogPostForm()
    return render(request, 'BLOG_POSTS/POST_FORM.html', {'form':form})

def post_list(request):
    BlogPosts = BlogPost.objects.all()
    return render(request, 'BLOG_POSTS/POST_LIST.html', {'BlogPosts':BlogPosts})

def post_update(request, id):
    blog_post_to_update = BlogPost.objects.get(id=id)
    form = BlogPostForm(request.POST, instance=blog_post_to_update)
    if form.is_valid():
        form.save()
        return redirect("POST_LIST")
    return render(request, 'BLOG_POSTS/POST_UPDATE.html', {'blog_post_to_update':blog_post_to_update})