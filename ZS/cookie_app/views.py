from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    visit_count = request.COOKIES.get('visit_count', '0')
    visit_count = int(visit_count) + 1
    response = render(request, 'count.html', {'visit_count':visit_count})
    response.set_cookie('visit_count', visit_count)
    return response


def delete_count(request):
    response = redirect('home')
    response.delete_cookie('visit_count')
    return response