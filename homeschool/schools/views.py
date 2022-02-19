from django.shortcuts import render
# from django.http import HttpResponse

def app(request):
  # return HttpResponse('Hello from app')
  context = {}
  return render(request, "schools/app.html", context)
