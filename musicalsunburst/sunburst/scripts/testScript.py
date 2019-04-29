# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 22:26:17 2019

@author: Jack
"""
def run():
    from django.http import HttpResponse
    from sunburst.models import Songs
    from collections import defaultdict
    nested_dict = defaultdict(
            lambda: defaultdict(
                lambda: defaultdict(list)
            )
        )
    for c in Songs.objects.all():
        nested_dict[c.fldYear][c.fldTerms][c.fnkArtist].append(c.fldTitle)
    def nested_to_tree(key, source):
        result = {'name': key, 'children':[]}
        for key, value in source.items():
            if isinstance(value, list):
                result['children'] = value
            else:
                child = nested_to_tree(key, value)
                result['children'].append(child)
    
        return result
    json = nested_to_tree('root', nested_dict)
    print(type(json))