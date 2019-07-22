from django.shortcuts import render

def index(request):
    template = 'blogging/index.html'
    context = {}
    return render(request, template, context)


def vueApp(request):
    template = 'blogging/vue-app.html'
    context = {}
    return render(request, template, context)
