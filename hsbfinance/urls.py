"""hsbfinance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from hsbfinance import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name="homepage"),
    path('services/', views.services, name="service"),
    path('about/', views.about, name="about"),
    path('partners/', views.partners, name="partners"),
    path('create/account/', views.createAccount,name="createAccount"),
    path('forget/password/',views.forgetPassword,name="forgetPassword"),
    path('user/',views.userIndex,name="userIndex"),
    path('loan/apply/',views.loanApply,name="loanApply"),
    path('loan/',views.loan,name="loan"),
    path('loan/status/',views.loanStatus,name="loanStatus"),
    path('userLogout/', views.userLogout, name="logout"),
    path('otp-verification/', views.otpVerification, name="otpVerification"),
    path('password-reset/', views.resetPassword, name="resetPassword"),
    path('profile/', views.profile, name="profile"),
    path('edit/profile/', views.edit_profile, name="edit_profile"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)