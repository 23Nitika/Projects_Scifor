from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import *
from .models import *
from django.http import HttpResponse
# Create your views here.

def home(request):
    if request.method == 'POST':
        print(request.POST)
        questions=QuesModel.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'result.html',context)
    else:
        questions=QuesModel.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'home.html',context)


def addQuestion(request):
    if request.user.is_staff:
        form=addQuestionform()
        if(request.method=='POST'):
            form=addQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'addQuestion.html',context)
    else:
        return redirect('home')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = createuserform()
        if request.method=='POST':
            form = createuserform(request.POST)
            if form.is_valid():
                user=form.save()
                return redirect('login')
        context ={
            'form':form,
        }
        return render(request, 'register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                # If authentication fails, return an error message or render the login page again with a message
                context = {'error_message': 'Invalid username or password'}
                return render(request, 'login.html', context)
        else:
            # If it's not a POST request, just render the login page
            return render(request, 'login.html')

def logoutPage(request):
    logout(request)
    return redirect('/')
        