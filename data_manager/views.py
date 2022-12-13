from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from data_manager.models import Events
from django.views import View
from django.http import HttpResponse,JsonResponse
import io,csv

# Create your views here.
class EventCreate(CreateView):
    model = Events
    fields = '__all__'
    # initial = {'date_of_death': '11/06/2020'}

class EventUpdate(UpdateView):
    model = Events
    fields = '__all__' # Not recommended (potential security issue if more fields added)

class EventDelete(DeleteView):
    model = Events
    # success_url = reverse_lazy('authors')

class BulkEventCreate(View):
    def post(self, request):
        user = request.user #get the current login user details
        paramFile = io.TextIOWrapper(request.FILES['employeefile'].file)
        portfolio1 = csv.DictReader(paramFile)
        list_of_dict = list(portfolio1)
        objs = [
                Events(
                country=row['first_name'],
                title=row['title'],
                date=row['date'],
                notes=row['notes'],
                bunting=True if row['bunting'] else False         
            )
            for row in list_of_dict
        ]
        try:
            msg = Events.objects.bulk_create(objs)
            returnmsg = {"status_code": 200}
            print('imported successfully')
        except Exception as e:
            print('Error While Importing Data: ',e)
            returnmsg = {"status_code": 500}       
        return JsonResponse(returnmsg)
