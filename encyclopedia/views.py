import random

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    if title in util.list_entries():
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "page_content": util.get_entry(title)
        })
    else:
        return HttpResponseNotFound("<h1>Error: Page not found.</h1>")
    

def search(request):
    if request.method == "GET":
        matching_entry = []
        # grab value within form
        query = request.GET.get('q','')
        if util.get_entry(query):
            return render(request, "encyclopedia/entry.html", {
                "title": query,
                "page_content": util.get_entry(query)
            })
        else: 
            entries = util.list_entries()
            # search entries for a substring of query
            
            for entry in entries:
                if query in entry:
                    matching_entry.append(entry)
                    break

            if matching_entry:
                return render(request, "encyclopedia/search-results.html", {
                    "matching_entry": matching_entry
                })
            
            else:
                return HttpResponseNotFound("<h1>No entries found</h1>")
    else: 
        return HttpResponseNotFound("<h1>Please only post to the proper pages!</h1>")
        
    
def new_page(request):
    if request.method == "POST":
        title = request.POST.get('title')
        markdown = request.POST['markdown']
        if title in util.list_entries():
            return HttpResponse("<h1>Article with title already exists.</h1>")
        else:
            util.save_entry(title, markdown)
            return render(request, "encyclopedia/entry.html", {
            "title": title,
            "page_content": util.get_entry(title)
        })
    else:
        return render(request, "encyclopedia/new-page.html")
    
def edit(request):
    if request.method == "GET":
        title = request.GET.get("title")
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "page_content": util.get_entry(title)
        })
    else:
        title = request.POST.get('title')
        markdown = request.POST['markdown']
        util.save_entry(title, markdown)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "page_content": util.get_entry(title)
        })
    
def random_page(request):
    if request.method == "GET":
        title = random.choice(util.list_entries())
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "page_content": util.get_entry(title)
        })
    else:
        return HttpResponseNotFound("<h1>Quit playing around!</h1>")
