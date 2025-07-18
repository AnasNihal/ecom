from django.urls import path
from eapp import views

urlpatterns = [
    path("",views.home, name="home"),
    path("products/",views.products,name = "products"),
    path("viewproduct/<int:p_id>/", views.viewproduct, name="viewproduct" ),
    path("filterproduct/", views.filterproduct , name="filterproduct"),
    path("register/",views.register, name="register"),
    path("login/",views.login, name="login"),
    path("logout/",views.logout, name="logout"),
    # path("profile/",views.profilepage,name="profile"),
    path('viewcart/',views.viewcart,name="viewcart"),
    path("addcart/<int:d_id>",views.addcart,name="addcart"),
    path('profile/addproduct',views.addproduct,name="addproduct"),
    path('profile/editproduct/<int:p_id>',views.editproduct,name="editproduct"),
    path('cart/increaseqty/<int:i_id>',views.increase_qty,name="increase_qty"),
    path('cart/decreaseqty/<int:i_id>',views.decrease_qty,name="decrease_qty"),
    path('cart/removeitem/<int:r_id>',views.remove_item,name="remove_item")

    ]
