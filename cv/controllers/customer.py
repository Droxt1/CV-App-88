from ninja import Router, File
from django.shortcuts import get_object_or_404
from cv.models import *
from typing import List
from cv.schema import *
from ninja.files import UploadedFile
from cv.data import *


customer_router = Router(tags=['customer'])


@customer_router.get('/', response=List[CustomerOut])
def get_all_customers(request):
    return CustomerProfile.objects.all()


@customer_router.get('/{customer_id}', response=CustomerOut)
def get_one_customer(request, customer_id: UUID4):
    return CustomerProfile.objects.get(id=customer_id)


@customer_router.put('/{customer_id}', response=CustomerProfileUpdate)
def update_customer(request, customer_id: UUID4, customer_in: CustomerProfileUpdate):
    customer = get_object_or_404(CustomerProfile, id=customer_id)
    customer.name = customer_in.name
    customer.phone = customer_in.phone
    customer.description = customer_in.description
    customer.address = customer_in.address
    customer.job_title = customer_in.job_title
    customer.Skills = customer_in.skills
    customer.language = customer_in.language

    customer.save()
    return customer


@customer_router.post('/{customer_id}/{job_id}')
def save_job(request, customer_id: UUID4, job_id: UUID4):
    job = Job.objects.get(id=job_id)
    customer = CustomerProfile.objects.get(id=customer_id)
    return customer.saved_job.add(job)


@customer_router.delete('/{customer_id}/{job_id}')
def delete_saved_job(request, customer_id: UUID4, job_id: UUID4):
    job = Job.objects.get(id=job_id)
    customer = CustomerProfile.objects.get(id=customer_id)
    return customer.saved_job.remove(job)


@customer_router.post('/get_all_ saved_jobs/', response=List[JobOut])
def get_all_saved_jobs(request, customer_id: UUID4):
    customer = CustomerProfile.objects.get(id=customer_id)
    return customer.saved_job.all()


@customer_router.post('/Aplly/', response=JobApplicationOut)
def apply_job(request, payload: JobApplicationIn):
    application = JobApplication.objects.create(**payload.dict())
    return application


"""Utliities"""


@customer_router.post('add_work_experience/', response=WorkExperienceOut)
def add_work_experience(request,  payload: WorkExperienceIn):
    qs = WorkExperience.objects.create(**payload.dict())
    return qs


@customer_router.put('update_work_experience/', response=WorkExperienceOut)
def update_work_experience(request, payload: WorkExperienceUpdateIn):
    qs = WorkExperience.objects.get(
        id=payload.id, customer_id=payload.customer_id)
    qs.company_worked_for = payload.company_worked_for
    qs.title = payload.title
    qs.start_date = payload.start_date
    qs.end_date = payload.end_date
    qs.save()
    return qs


@customer_router.delete('delete_work_experience/')
def delete_work_experience(request, payload: WKID):
    qs = WorkExperience.objects.get(
        id=payload.work_experience_id)
    qs.delete()
    return {'success': 'Work Experience deleted successfully'}


@customer_router.post('add_education/', response=EducationOut)
def add_education(request,  payload: EducationIn):
    qs = Education.objects.create(**payload.dict())
    return qs


@customer_router.put('update_education/', response=EducationOut)
def update_education(request, payload: EducationUpdateIn):
    qs = Education.objects.get(id=payload.id, customer_id=payload.customer_id)
    qs.school = payload.school
    qs.degree = payload.degree
    qs.start_date = payload.start_date
    qs.end_date = payload.end_date
    qs.save()
    return qs


@customer_router.delete('delete_education/')
def delete_education(request,payload: EDID):
    qs = Education.objects.get(id=payload.education_id)
    qs.delete()
    return {'success': 'Education deleted successfully'}
    


"""File Upload"""


@customer_router.post('/Image/', response=CustomerImage)
def upload_logo(request,  payload: CustomerId, image: UploadedFile = File(...)):
    qs = CustomerProfile.objects.get(id=payload.customer_id)

    def replace_old_image(self, image):
        if self.image:
            self.image.delete()
        self.image = image
        self.save()
    replace_old_image(qs, image)
    return qs


@customer_router.post('/CV/', response=CV)
def upload_cv(request,  payload: CustomerId, cv: UploadedFile = File(...)):
    qs = CustomerProfile.objects.get(id=payload.customer_id)

    def replace_old_cv(self, cv):
        if self.cv:
            self.cv.delete()
        self.cv = cv
        self.save()
    replace_old_cv(qs, cv)
    return qs
