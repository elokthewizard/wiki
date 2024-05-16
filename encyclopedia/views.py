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
        return HttpResponseNotFound("<h1>Page not found.</h1>")