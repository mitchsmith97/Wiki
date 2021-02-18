from django.shortcuts import render
from django.http import HttpResponse
import markdown2
from django import forms
from . import util

class searchForm(forms.Form):
    query = forms.CharField(label="Search Encyclopedia")


def check_for_entry(query):

    entriesList = util.list_entries()
    for entry in entriesList:
        if query in str(entry):
            return(query)



def index(request):

    requestString = str(request)
    print(requestString)
    if request == None:
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries(),
            "form": searchForm()
        })
    elif requestString.find("q="):
        requestString2 = requestString.split("q=")
        requestString3 = requestString2[1].split("'")
        query = requestString3[0]
        print(query)
        
        title = check_for_entry(query)

        print(title)


       
        return HttpResponse("WIP")

    else:
        return HttpResponse("WIP2")

def entry(request, title):
    marked_down = (util.get_entry(title))
    if marked_down == None:
        return HttpResponse("WIP3")
    htmld = markdown2.markdown(marked_down)

    if marked_down == None:
        return HttpResponse("Sorry, page does not exist")

    
    return render(request, "encyclopedia/entry.html", {
        "entry": htmld,
        "title": title,
        "form": searchForm()
    })



