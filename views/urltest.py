from django.shortcuts import render_to_response

def urltest(request):
    return render_to_response('urltest.html')