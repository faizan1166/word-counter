
from django.http import HttpResponse
from django.shortcuts import render
import re
import operator


def home(request):
    return render(request , 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    fulltext1 = re.sub('["@!#$%^&*(),.?/\`~:;.<>]','',fulltext)
    wordlist = fulltext1.split()

    worddictionary={}

    for word in wordlist:
        if word in worddictionary:
            #increase number
            worddictionary[word] += 1
        else:
            #add it to dictionary
            worddictionary[word] = 1

    sortcount = sorted(worddictionary.items() , key=operator.itemgetter(1) , reverse=True)

    return render(request,'count.html', {'fulltext' : fulltext , 'words' : len(wordlist) , 'sortedwords' : sortcount})
