from django.shortcuts import render


def handler500(request,exception):

    return render(request, '500.html')