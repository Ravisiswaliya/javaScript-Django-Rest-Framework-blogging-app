from django.shortcuts import render

def index(request):
    template = 'blogging/index.html'
    context = {}
    return render(request, template, context)

