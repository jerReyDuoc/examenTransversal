from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, UpdateView, DeleteView
from .forms import PostCreateForm
from .models import Post
from django.urls import reverse_lazy

# Create your views here.
class blogListView(View):
    def get(self,request,*args,**kwargs):
        posts = Post.objects.all()
        context={
            'posts':posts
        }
        return render(request, 'blog_list.html', context)
    
class blogCreateView(View):
    def get(self,request,*args,**kwargs):
        form=PostCreateForm()
        context={
            'form':form
        }
        return render(request, 'blog_create.html', context)
    
    def post(self,request,*args,**kwargs):
        if request.method=="POST":
            form=PostCreateForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data.get('title')
                content = form.cleaned_data.get('content')

                p, created = Post.objects.get_or_create(title=title, content=content)
                p.save()
                return redirect('blog:Home')
        context={

        }
        return render(request, 'blog_create.html', context)

class blogDetailView(View):

    def get(self,request, pk,*args,**kwargs):
        post = get_object_or_404(Post, pk=pk)
        context={
            'post':post
        }
        return render(request,'blog_detalle.html',context)
    