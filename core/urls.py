
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
