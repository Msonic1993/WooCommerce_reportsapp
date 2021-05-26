from django.shortcuts import redirect
from reportsapp.database_repository.models import Costs


def detail(request, id):
    if request.method == 'GET':
        sample = Costs.objects.get(id=id)
        sample.delete()
        return redirect('/costs/')
    return redirect('/costs/')



