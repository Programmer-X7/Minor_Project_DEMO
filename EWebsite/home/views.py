from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        "variable1":"This is sent by",
        "variable2":"Suman Mondal"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("This is HomePage")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is AboutPage")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("This is ServicesPage")

def contact(request):
    return render(request, 'contact.html')
    # return HttpResponse("This is ContactPage")
