from django.shortcuts import render
from django.http import HttpResponse
from sunburst.models import Songs
import random
from collections import defaultdict
import json

# Create your views here.
def index(request):
    return render(request, 'ajaxDemo/ajaxDemo.html')

def restReq(request):

    nested_dict = defaultdict(
        lambda: defaultdict(list)
    )

    maxResults = 1000
    year = request.GET.get('year', 0)
    for c in Songs.objects.filter(fldYear=year)[:maxResults]:
        nested_dict[str(c.fldTerms)][str(c.fnkArtist.fldName)].append(str(c.fldTitle))
        
    def nested_to_tree(key, source):
        result = {'name': key, 'children':[]}
        for key, value in source.items():
            if isinstance(value, list):
                result['children'].append(key)
                result['children'][-1] = { 'name' : key, 'children' : [{ 'name' : v, 'size' : 1} for v in value] }
            else:
                child = nested_to_tree(key, value)
                result['children'].append(child)
    
        return result
    
    jsonDict = nested_to_tree(str(year), nested_dict)
    return HttpResponse(json.dumps(jsonDict))
    
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

    