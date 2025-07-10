from django.urls import path
from eapp import views

urlpatterns = [
    path("",views.home, name="home"),
    path("products/",views.products,name = "products"),
    path("viewproduct/<int:p_id>/", views.viewproduct, name="viewproduct" ),
    path("filterproduct/", views.filterproduct , name="filterproduct")
]
