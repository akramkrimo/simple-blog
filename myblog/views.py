from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Comment
# Create your views here.
from django.views.generic import ListView, DetailView
from .forms import CreateBlog, AddComment
from django.http import HttpResponse

class BlogList(ListView):
    model = Blog
    template_name = 'myblog/list.html'
    queryset = Blog.objects.all()


def detail_view(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    if request.method=='POST':
        form = AddComment(request.POST)
        if form.is_valid():
            button = form.data.get('reply')
            if button is None:
                blog.comment_set.create(
                    user = request.user,
                    text = form.cleaned_data['comment']
                )
                return redirect('myblog:detail', slug=slug)
            else:
                #this is a mess that you gotta fix
                comment_id = form.data.get('reply')
                comment = Comment.objects.get(pk=comment_id)
                comment.replies.create(
                    blog=comment.blog,
                    text=form.cleaned_data['comment'],
                    user=request.user
                )
                return redirect('myblog:detail', slug=slug)
    else:
        form = AddComment()
        context = {
            'form': form,
            'object': blog
        }
        return render(request, 'myblog/detail.html', context)
        

# class BlogDetail(DetailView):
#     model = Blog
#     template_name = 'myblog/detail.html'

#     def get_object(self):
#         obj = super().get_object()
#         obj.number_of_reads +=1
#         obj.save()
#         return obj

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = 


def create_blog(request):
    if request.method == 'POST':
        form = CreateBlog(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            thumbnail = form.cleaned_data['thumbnail']
            blog = Blog(title=title,content=content, thumbnail=thumbnail,author=request.user)
            blog.save()            
            return redirect('myblog:list')
    else:
        form = CreateBlog()
        return render(request, 'myblog/create.html', {'form':form})
    # if request.method == 'POST':
    #     form = BlogForm(request.POST, request.FILES)
    #     print(form.errors)
    #     if form.is_valid():
    #         print(form.cleaned_data)
    #         blog = Blog(form, author=request.user)            
    #         blog.save()
    #         return redirect('myblog:list')
    # form = BlogForm()
    # return render(request, 'myblog/create.html', {'form':form})
