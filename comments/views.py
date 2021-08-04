
from .models import Comment, Post
from .forms import CommentForm
from django.shortcuts import render, redirect, reverse
from rest_framework import generics 
from .serializers import PostSer, CommentsSer

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSer 

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentsSer

def post_detail(request):
    post = Post.objects.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            reply_obj = None
            try:
                reply_id = int(request.POST.get('reply_id'))
            except:
                reply_id = None
            if reply_id:
                reply_obj = Comment.objects.get(id=reply_id)

            author = form.cleaned_data['author']
            comment = form.cleaned_data['comment']
            if reply_obj:
               Comment(author=author,comment_field=comment, reply=reply_obj, post=post).save()
            else:
                Comment(author=author,comment_field=comment, post=post).save()
            return redirect(reverse('post_detail'))
    else:
        form = CommentForm()
    comments = Comment.objects.filter(post=post, reply=None).order_by('-date_created')
    context = {
        'post':post,
        'form':form,
        'comments':comments
    }
    return render(request, 'post_detail.html', context)
