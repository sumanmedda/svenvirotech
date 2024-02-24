"""
Developed By : Digiprayas

"""
from django.contrib import admin
from django.urls import path, reverse_lazy
from django.views.generic.base import RedirectView
from ecom import views

admin.site.site_header = "Siddhivinayak Envirotech"
admin.site.site_title = "SVE Portal"
admin.site.index_title = "SVE Admin Portal"

urlpatterns = [
    path('admin/', RedirectView.as_view(url=reverse_lazy('admin:index'))),
    path('admin2/', admin.site.urls),
    path('',views.home_view,name=''),
    path('gallery', views.gallery_view,name='gallery'),
    path('allproducts', views.allproducts_view,name='allproducts'),
    path('single-product/<int:pk>', views.single_product_view,name='single-product'),
]
