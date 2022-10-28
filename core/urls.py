"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from ninja import NinjaAPI
from cv.Auth.API.comapny import company_auth_router
from cv.Auth.API.customer import customer_auth_router
from cv.controllers.customer import customer_router
from cv.controllers.company import company_router
from cv.controllers.application import application_router
from cv.controllers.job import job_router
from cv.controllers.meta import meta_router
from django.conf import settings
from django.conf.urls.static import static
from cv.Auth.API.GlobalSignIn import sign_in_router
from django_otp.admin import OTPAdminSite

api = NinjaAPI(version='1.0', title='CV API', description='CV API  Alpha')

api.add_router('jobs/', job_router)
api.add_router('customers/', customer_router)
api.add_router('companies/', company_router)
api.add_router('applications/', application_router)
api.add_router('meta/', meta_router)
api.add_router('auth/', company_auth_router)
api.add_router('auth/', customer_auth_router)
api.add_router('auth/', sign_in_router)
admin.site.__class__ = OTPAdminSite

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path("api/", api.urls),


              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.MEDIA_URL,
                                                                                         document_root=settings.MEDIA_ROOT)
