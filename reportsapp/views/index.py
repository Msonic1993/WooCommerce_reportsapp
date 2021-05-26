from django.shortcuts import render
from django.views.decorators.http import require_http_methods


@require_http_methods(["POST", "GET"])
def index(request):
    return render(request, 'glowna.html', {})