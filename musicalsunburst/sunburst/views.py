from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def index(request):
    return render(request, 'ajaxDemo/ajaxDemo.html')

def restReq(request):
    results = ['It is certain.',
     'It is decidedly so.',
     'Without a doubt.',
     'Yes - definitely.',
     'You may rely on it.',
     'As I see it, yes.',
     'Most likely.',
     'Outlook good.',
     'Yes.',
     'Signs point to yes.',
     'Reply hazy, try again.',
     'Ask again right now.',
     'Better not tell you now.',
     'Cannot predict now.',
     'Concentrate and ask again.',
     "Don't count on it.",
     'My reply is no.', 
     'My sources say no.',
     'Outlook not so good.',
     'Very doubtful.']
    
    result = results[random.randint(0, 20)]
    
    return HttpResponse(result)
    