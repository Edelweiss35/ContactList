from django.views.generic import ListView
from django.http.response import JsonResponse
from django.core import serializers
import json
from contact_list.models import Book
from django.forms import ModelForm
from django.shortcuts import get_object_or_404

class BookList(ListView):
    model = Book

class UserForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'e_mail', 'phone_number']

def contactlists(request):
    users = Book.objects.all()
    posts_serialized = serializers.serialize('json', users)
    return JsonResponse(posts_serialized, safe=False)

def contactlists_add(request):
    form = UserForm(json.loads(request.body) or None)
    if form.is_valid():
        form.save()
    return JsonResponse(json.loads(request.body))

def contactlists_get(request):
    id_json = json.loads(request.body)
    id = id_json["id"]
    users = Book.objects.all().filter(id=id)
    posts_serialized = serializers.serialize('json', users)
    return JsonResponse(posts_serialized, safe=False)

def contactlists_update(request):
    json_data = json.loads(request.body)
    user = get_object_or_404(Book, pk=json_data["id"])
    form = UserForm(json_data["user"], instance=user)
    if form.is_valid():
        form.save()
    return JsonResponse(json_data, safe=False)

def contactlists_delete(request):
    id_json = json.loads(request.body)
    id = id_json["id"]
    user = get_object_or_404(Book, pk=id)
    user.delete()
    return JsonResponse(json.loads(request.body), safe=False)