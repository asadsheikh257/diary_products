"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from app import views
from django.contrib.auth import views as auth_view
from app.forms import *

urlpatterns = [

    path('', Home, name="home"),
    path('about/', About, name="about"),
    path('contact/', Contact, name="contact"),
    path('category/<slug:val>', Category, name="category"),
    path('category-title/<val>', CategoryTitle, name="category-title"),
    path('product_detail/<id>', ProductDetail, name="product_detail"),
    path('profile/', ProfileView, name="profile"),
    # path('profile/', views.ProfileView.as_view(), name="profile"),
    path('address/', AddressView, name="address"),
    path('updateAddress/<int:id>', UpdateAddress, name="updateAddress"),

    # login_authentication

    # path('registration/', views.CustomerRegistrationView.as_view(),
    #      name="register"),
    path('registration/', CustomerRegistrationView, name='register'),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='app/login.html',
         authentication_form=LoginForm), name='login'),
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='app/password_reset.html',
         form_class=MyPasswordResetForm), name='password-reset'),





    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
