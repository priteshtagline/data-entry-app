from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from data_manager.models import Events
from django.views import View
from django.http import JsonResponse
import io,csv
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import CreateEventForm
from .models import Countries
class EventCreate(CreateView):
    model = Events
    fields = '__all__'
    success_url = reverse_lazy('/event')
   

class EventUpdate(UpdateView):
    model = Events
    fields = '__all__' 

class EventDelete(DeleteView):
    model = Events
class BulkEventCreate(View):
    def post(self, request, *args, **kwargs):
        paramFile = io.TextIOWrapper(request.FILES['bulkcreatfile'].file)
        portfolio1 = csv.DictReader(paramFile)
        list_of_dict = list(portfolio1)
        try:
            objs = [
                    Events(
                    country= Countries.objects.get(name=row["country"]),
                    title=row['title'],
                    date=row['date'],
                    notes=row['notes'],
                    bunting=True if row['bunting'] else False         
                )
                for row in list_of_dict
            ]
        except:
            print('imported successfully')
        try:
            Events.objects.bulk_create(objs)
            print('imported successfully')
        except Exception as e:
            print('Error While Importing Data: ',e)
            returnmsg = {"status_code": 500}       
        return redirect("/event")

class InventoryListView(LoginRequiredMixin, ListView):
    model = Events
    fields = "__all__"
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["event_form"] = CreateEventForm
        return context
