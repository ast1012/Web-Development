from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #return HttpResponse('''<h1>Hello world!<h1> <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7"> Django Course Click Here <a\>''')
    return render(request, 'index.html')
    
def about(request):
    return HttpResponse("This is about page !!")

def analyze(request):
    #Collect the text here
    djtext = request.GET.get('text', 'default')
    
    #check vaues of checkboxes
    removepunc = request.GET.get('removepunc', 'off')
    capitals = request.GET.get('capitals', 'off')
    spaces = request.GET.get('spaces', 'off')
    counts = request.GET.get('counts', 'off')
    puntutations = '''!()-[];:'"\,<>.?@#$%^&*_~|'''
    
    #Remove Puntuation
    if removepunc=='on':
        analyse = ''
        for char in djtext:
            if char not in puntutations:
                analyse = analyse+char
        params = {'purpose':'Remove Puntutation', 'analyzed_text':analyse}
        return render(request, 'analyze.html', params)
    
    #Make Capitals
    if capitals=="on":
        analyse = ''
        for char in djtext:
            analyse = analyse + char.upper()
        params = {'purpose':'First Letter Capitalized', 'analyzed_text':analyse}
        return render(request, 'analyze.html', params)
    
    #Remove Extra Spaces
    if spaces=='on':
        analyse = ''
        for index, char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyse = analyse + char
        params = {'purpose':'Spaces Removed', 'analyzed_text':analyse}
        return render(request, 'analyze.html', params)
    
    #Return number of Characters
    if counts=='on':
        count = len(djtext)
        params = {'purpose':'Number of words is', 'analyzed_text':count}
        return render(request, 'analyze.html', params)
    
    #Else return Error
    else:
        return render(request, 'err_msg.html' )
