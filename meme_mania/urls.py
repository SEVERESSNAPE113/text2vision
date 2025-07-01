"""
URL configuration for meme_mania project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from backoffice_engine import views
from meme_mania import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('index/', views.index),
    path('about/', views.about),
    path('blog_details/', views.blog_details),
    path('blog/', views.blog),
    path('contact/', views.contact),
    path('e/', views.e),
    path('img/', views.img),
    path('login/', views.login),
    path('portfolio_detail/', views.portfolio_details),
    path('portfolio/', views.portfolio),
    path('price/', views.price),
    path('services/', views.services),
    path('t_params/', views.t_params),
    path('team/', views.team),
    path('index_1/', views.index_1),
    path('index_3/', views.index_3),
    path('registration/', views.registration),
    path('profile/', views.profile), 
    path('send_otp/', views.send_otp),
    path('reset_pass/', views.reset_pass),   
    path('logout/', views.logout),
    path('delete_account/<int:id>', views.delete_account),
    path('update_profile/<int:id>', views.update_profile),
    path('generate_image/', views.generate_image),
    path('show/', views.show),
    path('gallery/', views.gallery),
    path('payment/', views.payment),
    path('feedback/', views.feedback),
    path('check/',views.check)
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

