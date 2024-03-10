from django.shortcuts import render, get_object_or_404
from core.models import Comment
from core.spam_model import predict_spam 
from django.http import HttpResponse

##added
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout




# Create your views here.


## Added 

def home(request):
    return render(request, "index.html")

def signup(request):
    template = 'signup.html'
    if request.method=="POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if User.objects.filter(username=username):
            messages.error(request, "Username already exists! Please try another username")
            return redirect('home')
        
        
        if User.objects.filter(email=email):
            messages.error(request, "Email already registered!")
            return redirect('home')
        
        if len(username)>10:
            messages.error(request, "Username must be under 10 characters.")
            
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't match!")
            
        
        if not username.isalnum():
            messages.error(request, "Username must be alphanumeric!")
            return redirect('home')
        


        myuser = User.objects.create_user(username, email, pass1)
        myuser.is_staff = True
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Your account has been successfully created")


        # Welcome Email

        subject = "Spam Message Detection"
        message = "Hello" + myuser.first_name + "!! \n" +""






        return redirect('/signin')

    return render(request, "signup.html")



def signin(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('pass1')
       

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "comments.html", {'fname': fname})
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('home')

    return render(request, "signin.html")

def comments(request):
    comments = Comment.objects.all()
    context = {'comments':comments}
    return render(request, 'comments.html',context)

def check_spam(request):
    comments = Comment.objects.all()
    predictions = predict_spam(comments.values_list('text', flat=True))
    print(predictions)
    context = {'comments':zip(comments, predictions)}
    return render(request, 'partials/comments-spam.html',context)

def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return HttpResponse(status=204)


def signout(request):
    logout(request)
    messages.success(request, "Logged out Successfully")
    return redirect("home")