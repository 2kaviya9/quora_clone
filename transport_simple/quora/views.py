from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, QuoraPostForm, QuoraReplyForm
from .models import QuoraPost, QuoraReply

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home_view(request):
    posts = QuoraPost.objects.all()
    return render(request, 'home.html', {'posts': posts})

@login_required
def post_create_view(request):
    if request.method == 'POST':
        form = QuoraPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.created_by = request.user
            post.save()
            return redirect('home')
    else:
        form = QuoraPostForm()
    return render(request, 'post_create.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(QuoraPost, pk=pk)
    return render(request, 'post_detail.html', {'post': post})


@login_required
def post_detail_view(request, post_id):
    post = get_object_or_404(QuoraPost, id=post_id)
    replies = post.replies.all()
    if request.method == 'POST':
        form = QuoraReplyForm(request.POST, request.FILES)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.post = post
            reply.user = request.user
            reply.created_by = request.user
            reply.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = QuoraReplyForm()
    print( {'post': post, 'replies': replies, 'form': form})
    return render(request, 'post_detail.html', {'post': post, 'replies': replies, 'form': form})

@login_required
def like_reply_view(request, reply_id):
    reply = get_object_or_404(QuoraReply, id=reply_id)
    reply.likes.add(request.user)
    return redirect('post_detail', post_id=reply.post.id)

@login_required
def like_post(request, post_id):
    post = get_object_or_404(QuoraPost, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('post_detail', post_id=post.id)
