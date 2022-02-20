from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse

@login_required
def app(request):
  # return HttpResponse('Hello from app')
  context = {}
  return render(request, "schools/app.html", context)
