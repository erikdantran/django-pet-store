from django.urls import path

from . import views

app_name = 'pets'
urlpatterns = [
  path('', views.IndexView.as_view(), name='index'),
  path('add_pet', views.add_pet, name='add_pet'),
  path('search', views.search, name='search'),
  path('<int:pet_id>/', views.DetailView.as_view(), name='detail'),
]



# path('add_pet', views.AddPetView.as_view(), name='add_pet'),
# path('<int:pet_id>/purchase/', views.purchase, name='purchase'),
# path('<int:pet_id>/delete/', views.delete, name='delete'),