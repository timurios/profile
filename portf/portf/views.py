from django.shortcuts import render, redirect, HttpResponse

def main(request):
    return render(request, "tmp/index.html")

def about(request):
    return render(request, "tmp/about.html")



 







