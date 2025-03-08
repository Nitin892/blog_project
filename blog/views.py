from django.shortcuts import render,redirect,get_object_or_404
from .models import Post,Comment
from .forms import PostForm, LoginForm,AddCommentForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, 'blog/index.html')
    

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('list-post')
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request,'blog/login.html',{'form':form})


def user_registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request,"Password mismatched")
            return redirect('registration')
        data = {
            'username' : username,
            'email' : email,
            'password' : password
        }
        user = User.objects.create_user(**data)
        login(request, user)
        messages.success(request, "successful")
        return redirect('list-post')
    else:
        return render(request, 'blog/registration.html') 

def list_posts(request):
    context = {'posts' : Post.objects.all().order_by('-id')}  
    return render(request, 'blog/listpost.html', context)

@login_required
def create_post(request):
    if request.method=='POST':
        form  = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  
            post.author = request.user  
            post.save()
            return redirect('list-post')  
    else:
        form = PostForm()
    return render(request,'blog/createpost.html',{"form":form})

def retrive_posts(request, id):
    context = {'posts': [Post.objects.get(id = id)]}

    return render(request, 'blog/listpost.html', context)



def view_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comment_data = Comment.objects.filter(post = post)
    print("*"*10)
    print(comment_data)
    print("*"*10)
    return render(request, 'blog/view_post.html', {'post': post,'comments':comment_data})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('view_post', post_id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})


def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('list-post')  


def add_comment_post(request, id):
    if request.method=='POST':
        form = AddCommentForm(request.POST)
        post_object = Post.objects.get(id = id)
        if form.is_valid():
            post = form.save(commit=False) 
            post.post =  post_object
            post.author = request.user  
            form.save()
            return redirect('view_post', post_id = id)
    else:
        form = AddCommentForm()
        return render(request, 'blog/addcomments.html',{'form':form})
    