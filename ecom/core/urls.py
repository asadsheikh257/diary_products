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
    path('product-detail/<id>', ProductDetail, name="product_detail"),
    path('profile/', ProfileView, name="profile"),
    path('address/', AddressView, name="address"),
    path('updateAddress/<int:id>', UpdateAddress, name="updateAddress"),

    # login_authentication
    path('registration/', CustomerRegistrationView, name='register'),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='app/login.html',
         authentication_form=LoginForm), name='login'),
    path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='app/changepassword.html',
         form_class=MyPasswordChangeForm, success_url='/passwordchangedone'), name='passwordchange'),
    path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(
        template_name='app/password_change_done.html'), name='passwordchangedone'),
    path('logout/', auth_view.LogoutView.as_view(next_page='/'), name='logout'),

    path('password-reset/', auth_view.PasswordResetView.as_view(
        template_name='app/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(
        template_name='app/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(
        template_name='app/password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(
        template_name='app/password_reset_complete.html'), name='password_reset_complete'),

    # cart
    path('add-to-cart/', AddToCart, name='add_to_cart'),
    path('cart/',ShowCart, name='showcart'),
    path('pluscart/', Plus_Cart),
    path('minuscart/', Minus_Cart),
    path('removecart/', Remove_Cart),



    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
