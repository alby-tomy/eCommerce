from django.urls import path
from . import views

app_name = 'e_commerceApp'

urlpatterns = [
    path('',views.allProdCatView, name='allProdCatName'),
    path('<slug:c_slug>/',views.allProdCatView, name='products_by_cat'),
    path('<slug:c_slug>/<slug:p_slug>',views.proDetailView, name='proDetailName')
]