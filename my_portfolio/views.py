from django.http import HttpResponse
from django.shortcuts import render



def homePage(request):

    return render (request,'index.html')


def aboutPage(request):
    return render (request,'about.html')




def skillsPage(request):
    return render (request,'skills.html')




def blogPage(request):
    return render (request,'blog.html')

