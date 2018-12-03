from django.urls import path

from . import views

app_name = 'contact_list'

urlpatterns = [
  path('', views.BookList.as_view(), name='book_list'),
  path('contactlists', views.contactlists, name='contactlists'),
  path('contactlists_add', views.contactlists_add, name='contactlists_add'),
  path('contactlists_delete', views.contactlists_delete, name='contactlists_delete'),
  path('contactlists_update', views.contactlists_update, name='contactlists_update'),
  path('contactlists_get', views.contactlists_get, name='contactlists_get'),
]