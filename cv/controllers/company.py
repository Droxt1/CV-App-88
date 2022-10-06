from django.db.models import Q
from django.shortcuts import get_object_or_404
from ninja import Router, File
from ninja.files import UploadedFile
from rest_framework import status

from cv.Auth.Authorization import CompanyAuth
from cv.models import CompanyProfile
from cv.schema import *

company_router = Router(tags=['company'])


@company_router.get('/', response=List[CompanyOut], )
def get_all_company(request):
    return status.HTTP_200_OK, CompanyProfile.objects.all()


@company_router.get('/search', response=List[CompanySearchResult])
def search_company(request, company_name: str):
    try:

        q = Q(name__icontains=company_name)
        return CompanyProfile.objects.filter(q)
    except:
        return status.HTTP_400_BAD_REQUEST, {'error': 'something went wrong'}


@company_router.get('/{company_id}', response=CompanyOut)
def get_one_company(request, company_id: UUID4):
    return CompanyProfile.objects.get(id=company_id)


@company_router.put('/{company_id}', response=CompanyProfileUpdate, auth=CompanyAuth())
def update_company(request, company_id: UUID4, company_in: CompanyProfileUpdate, ):
    company = get_object_or_404(CompanyProfile, id=company_id)
    company.name = company_in.name
    company.phone = company_in.phone
    company.description = company_in.description
    company.address = company_in.address
    company.save()
    return company


@company_router.post('/Image/', response={200: CompanyImage, 400: FourOFour}, auth=CompanyAuth())
def upload_logo(request, company_id: UUID4, image: UploadedFile = File(...)):
    try:
        qs = CompanyProfile.objects.get(id=company_id)

        def replace_old_image(self, image):
            if self.image:
                self.image.delete()
            self.image = image
            self.save()

        if image.content_type == 'image/jpeg' or image.content_type == 'image/png' or image.content_type == 'image/jpg':
            replace_old_image(qs, image)
            return qs
        else:
            return status.HTTP_400_BAD_REQUEST, {'error': 'image format not supported'}
    except:
        return status.HTTP_400_BAD_REQUEST, {'error': 'something went wrong'}

# search company query
