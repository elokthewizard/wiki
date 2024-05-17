from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    if util.get_entry(title):
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "page_content": util.get_entry(title)
        })
    else:
        return HttpResponseNotFound("<h1>Error: Page not found.</h1>")
    

def search(request):
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
        
        for entry in entries:
            if query in entry:
                matching_entry.append(entry)
                break

        if matching_entry:
            return render(request, "encyclopedia/search-results.html", {
                "matching_entry": matching_entry
            })
        # search entries for a substring of query
        else:
            return HttpResponseNotFound("<h1>Pardon the dust, WIP</h1>")