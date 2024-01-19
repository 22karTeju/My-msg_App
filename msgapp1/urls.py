from django.urls import path
from msgapp1 import views

urlpatterns = [
   path('create',views.create),
   path('dashboard',views.Dashboard),
   path('delete/<rid>',views.delete),
   path('edit/<rid>',views.edit)
]