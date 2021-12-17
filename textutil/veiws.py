# i have created this website
from django import http
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    # pars={'name':'vaibhav','sarname':'sharma'}
    return render(request,'index.html')
def analyze(request):
    txt=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newline=request.POST.get('newline','off')
    extraspace=request.POST.get('extraspace','off')
    print(removepunc)
    print(txt)
    if removepunc=="on":

        # analyzed=txt
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=''
        for char in txt:
            if char not in punc:
                analyzed=analyzed+char
        params={'purpose':'remove punctuation','analyze_text':analyzed}
        txt=analyzed
        # return render(request,'analyze.html',params)
    if (fullcaps=="on"):
        analyzed=""
        analyzed=analyzed+txt.upper()
        params={"purpose":"chenged to uppercase","analyze_text":analyzed}
        txt=analyzed
        # return render(request,"analyze.html",params)
    if (extraspace=="on"):
        analyzed=""
        for index in range(len(txt)-1):
            if txt[index]==" " and txt[index+1]==" ":
                pass
            else:
                analyzed=analyzed+txt[index]
        params={"purpose":"chenged to uppercase","analyze_text":analyzed}
        txt=analyzed
        # return render(request,"analyze.html",params)
    if (newline=="on"):
        analyzed=""
        for char in txt:
            if char!="\n" and char!="\r":
                analyzed=analyzed+char
        params={"purpose":"without any extra line","analyze_text":anaplyzed}
        txt=analyzed
        # return render(request,"analyze.html",params)
    if (newline!="on" and extraspace!="on" and fullcaps!="on" and removepunc!="on"):
        return HttpResponse("error")

    return render(request,"analyze.html",params)
