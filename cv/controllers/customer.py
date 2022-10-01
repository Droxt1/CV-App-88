from ninja import Router, File
from django.shortcuts import get_object_or_404
from rest_framework import status
from cv.Auth.Authorization import CustomerAuth
from cv.models import *
from typing import List
from cv.schema import *
from ninja.files import UploadedFile
from cv.data import *
from ninja.pagination import paginate
customer_router = Router(tags=['customer'])


@customer_router.get('/', response={200: List[CustomerOut], 400: FourOFour})
def get_all_customers(request):
    try:
        return status.HTTP_200_OK, CustomerProfile.objects.all()
    except:
        return status.HTTP_400_BAD_REQUEST, {'error': 'something went wrong'}


@customer_router.get('/{customer_id}', response={200: CustomerOut, 404: FourOFour})
def get_one_customer(request, customer_id: UUID4):
    try:
        return status.HTTP_200_OK, CustomerProfile.objects.get(id=customer_id)
    except CustomerProfile.DoesNotExist:
        return status.HTTP_404_NOT_FOUND, {'error': 'customer not found'}


@customer_router.put('/{customer_id}', response={202: CustomerProfileUpdate, 404: FourOFour})
def update_customer(request, customer_id: UUID4, customer_in: CustomerProfileUpdate):
    try:
        customer = get_object_or_404(CustomerProfile, id=customer_id)
        customer.name = customer_in.name
        customer.phone = customer_in.phone
        customer.description = customer_in.description
        customer.address = customer_in.address
        customer.job_title = customer_in.job_title
        customer.Skills = customer_in.skills
        customer.language = customer_in.language

        customer.save()
        return status.HTTP_202_ACCEPTED, customer
    except (CustomerProfile.DoesNotExist):
        return status.HTTP_404_NOT_FOUND, {'error': 'customer not found'}


@customer_router.post('/{customer_id}/{job_id}')
def save_job(request, customer_id: UUID4, job_id: UUID4, ):
    try:
        job = Job.objects.get(id=job_id)
        customer = CustomerProfile.objects.get(id=customer_id)
        return customer.saved_job.add(job)
    except CustomerProfile.DoesNotExist:
        return status.HTTP_404_NOT_FOUND, {'error': 'customer not found'}


@customer_router.delete('/{customer_id}/{job_id}',)
def delete_saved_job(request, customer_id: UUID4, job_id: UUID4):
    job = Job.objects.get(id=job_id)
    customer = CustomerProfile.objects.get(id=customer_id)
    return customer.saved_job.remove(job)


@customer_router.post('/get_all_ saved_jobs/', response={200: List[JobOut], 204: FourOFour})
@paginate
def get_all_saved_jobs(request, customer_id: UUID4):
    try:
        customer = CustomerProfile.objects.get(id=customer_id)
        return customer.saved_job.all()
    except CustomerProfile.saved_job.isnull():
        return status.HTTP_204_NO_CONTENT, {'error': 'Customer Has No Saved Jobs'}


@customer_router.post('/Aplly/', response={200: JobApplicationOut, 400: FourOFour})
def apply_job(request, payload: JobApplicationIn):
    try:
        application = JobApplication.objects.create(**payload.dict())
        return status.HTTP_200_OK, application
    except:
        return status.HTTP_400_BAD_REQUEST, {'error': 'something went wrong'}


"""Utliities"""


@customer_router.post('add_work_experience/', response={201: WorkExperienceOut, 400: FourOFour})
def add_work_experience(request, payload: WorkExperienceIn):
    try:
        qs = WorkExperience.objects.create(**payload.dict())
        return status.HTTP_201_CREATED, qs
    except:
        return status.HTTP_400_BAD_REQUEST, {'error': 'something went wrong'}


@customer_router.put('update_work_experience/', response={200: WorkExperienceOut, 422: FourOFour})
def update_work_experience(request, payload: WorkExperienceUpdateIn):
    try:
        qs = WorkExperience.objects.get(
            id=payload.id, customer_id=payload.customer_id)
        qs.company_worked_for = payload.company_worked_for
        qs.title = payload.title
        qs.start_date = payload.start_date
        qs.end_date = payload.end_date
        qs.save()
        return status.HTTP_200_OK, qs
    except:
        return {'error': 'something went wrong'}, status.HTTP_422_UNPROCESSABLE_ENTITY


@customer_router.delete('delete_work_experience/')
def delete_work_experience(request, payload: WKID):
    qs = WorkExperience.objects.get(
        id=payload.work_experience_id)
    qs.delete()
    return {'success': 'Work Experience deleted successfully'}


@customer_router.post('add_education/', response={201: EducationOut, 400: FourOFour})
def add_education(request, payload: EducationIn):
    try:
        qs = Education.objects.create(**payload.dict())
        return status.HTTP_201_CREATED, qs
    except:
        return status.HTTP_400_BAD_REQUEST, {'error': 'something went wrong'}


@customer_router.put('update_education/', response={201: EducationOut, 422: FourOFour})
def update_education(request, payload: EducationUpdateIn):
    try:
        qs = Education.objects.get(
            id=payload.id, customer_id=payload.customer_id)
        qs.school = payload.school
        qs.degree = payload.degree
        qs.start_date = payload.start_date
        qs.end_date = payload.end_date
        qs.save()
        return status.HTTP_201_CREATED, qs
    except:
        return {'error': 'something went wrong'}, status.HTTP_422_UNPROCESSABLE_ENTITY


@customer_router.delete('delete_education/')
def delete_education(request, payload: EDID):
    qs = Education.objects.get(id=payload.education_id)
    qs.delete()
    return {'success': 'Education deleted successfully'}


"""File Upload"""


@customer_router.post('/Image/', response={
    200: CustomerImage,
    400: FourOFour
})
def upload_logo(request, payload: CustomerId, image: UploadedFile = File(...)):
    try:
        qs = CustomerProfile.objects.get(id=payload.customer_id)

        def replace_old_image(self, image):
            if self.image:
                self.image.delete()
            self.image = image
            self.save()
        if image.content_type == 'image/jpeg' or image.content_type == 'image/png' or image.content_type == 'image/jpg':
            replace_old_image(qs, image)
            return status.HTTP_200_OK, qs
        else:
            return status.HTTP_400_BAD_REQUEST, {'error': 'File type not supported'}
    except:
        return status.HTTP_400_BAD_REQUEST, {'error': 'something went wrong'}


@customer_router.post('/CV/', response={200: CV,
                                        400: FourOFour})
def upload_cv(request, payload: CustomerId, cv: UploadedFile = File(...)):
    try:
        qs = CustomerProfile.objects.get(id=payload.customer_id)

        def replace_old_cv(self, cv):
            if self.cv:
                self.cv.delete()
            self.cv = cv
            self.save()
        if cv.content_type == 'application/pdf':
            replace_old_cv(qs, cv)
            return status.HTTP_200_OK, qs
        else:
            return status.HTTP_400_BAD_REQUEST, {'error': 'File type not supported'}
    except:
        return status.HTTP_400_BAD_REQUEST, {'error': 'something went wrong'}
