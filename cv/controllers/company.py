from ninja import Router, File
from django.shortcuts import get_object_or_404
from cv.models import *
from typing import List
from cv.schema import *
from ninja.files import UploadedFile
from cv.data import *


company_router = Router(tags=['company'])


@company_router.get('/', response=List[CompanyOut])
def get_all_company(request):
    profiles = CompanyProfile.objects.all()
    return profiles


@company_router.get('/{company_id}', response=CompanyOut)
def get_one_company(request, company_id: UUID4):
    return CompanyProfile.objects.get(id=company_id)


@company_router.post('/search_company/{company_name}', response=List[CompanyJobOut])
def search_company(request, company_name: str):
    return CompanyProfile.objects.filter(name__icontains=company_name)


@company_router.put('/{company_id}', response=CompanyProfileUpdate)
def update_company(request, company_id: UUID4, company_in: CompanyProfileUpdate):
    company = get_object_or_404(CompanyProfile, id=company_id)
    company.name = company_in.name
    company.phone = company_in.phone
    company.description = company_in.description
    company.address = company_in.address
    company.save()
    return company


@company_router.post('/Image/', response=CompanyImage)
def upload_logo(request, company_id: UUID4, image: UploadedFile = File(...)):
    qs = CompanyProfile.objects.get(id=company_id)

    def replace_old_image(self, image):
        if self.image:
            self.image.delete()
        self.image = image
        self.save()
    replace_old_image(qs, image)
    return qs
