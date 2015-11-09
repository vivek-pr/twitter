from django.shortcuts import render
from .models import Tweets,Tweeter
from .forms import TweetForm, UserForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
# Create your views here.


def home(request):
    if "user" in request.session:
        u1=User.objects.get(username=request.session["user"])
        #import pdb; pdb.set_trace()
        t1=Tweeter.objects.get(user=u1)
        folowing=t1.following.all()

        all_tweets=Tweets.objects.filter(Q(author=u1) | Q(author__in=folowing))
        context={
        'forms':TweetForm(),
        'tweets':all_tweets
        }
        return render(request,'tweets.html',context)
    else:
        context={
        'forms':UserForm()
        }
        return render(request,'login.html',context)


def login(request):
    if request.method=='POST':
        form=UserForm(data=request.POST)

        user = authenticate(username=form.data['username'], password=form.data['password'])
        if user is not None:
            request.session['user']=form.data['username']
            u1=User.objects.get(username=request.session["user"])
            t1=Tweeter.objects.get(user=u1)
            folowing=t1.following.all()

            all_tweets=Tweets.objects.filter(Q(author=u1) | Q(author__in=folowing))
            context={
            'forms':TweetForm(),
            'tweets':all_tweets
            }
            return render(request,'tweets.html',context)
        else:
            message='You are not authorized '
            return render(request,'login.html',{'forms':UserForm(),'message':message})


def StoreTweet(request):
    if request.method=='POST':
        form=TweetForm(data=request.POST)

        tweets=Tweets(text=form.data['text'],author=User.objects.get(username=request.session['user']))
        tweets.save()
        u1=User.objects.get(username=request.session["user"])
        t1=Tweeter.objects.get(user=u1)
        folowing=t1.following.all()

        all_tweets=Tweets.objects.filter(Q(author=u1) | Q(author__in=folowing))
        context={
        'forms':TweetForm(),
        'tweets':all_tweets
        }
        return render(request,'tweets.html',context)


