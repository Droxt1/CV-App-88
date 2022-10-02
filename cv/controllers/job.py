from ninja.pagination import RouterPaginated, PageNumberPagination, LimitOffsetPagination, paginate
from django.shortcuts import get_object_or_404

from cv.Auth.Authorization import CompanyAuth
from cv.models import *
from typing import List
from cv.schema import *
from cv.data import *
from rest_framework import status

job_router = RouterPaginated(tags=['Jobs'])


@job_router.get('/', response={200: List[JobSchema], 400: FourOFour})
@paginate
def get_all_jobs(request):
    try:
        jobs = Job.objects.all().order_by('-created')
        return jobs
    except:
        return {'error': 'something went wrong'}, status.HTTP_400_BAD_REQUEST


@job_router.get('/featured_jobs_path_params', response={
    200: List[JobSchema],
    404: FourOFour,

})
def get_featured_jobs(request):
    try:
        jobs = Job.objects.filter(is_featured=True).order_by("-created").all()
        return status.HTTP_200_OK, jobs
    except Job.DoesNotExist:
        return status.HTTP_404_NOT_FOUND, {'error': 'no featured jobs found'}


@job_router.get('/{job_id}', response={
    200: JobSchema,
    404: FourOFour,
})
def get_one_job(request, job_id: UUID4):
    try:
        return Job.objects.get(id=job_id)
    except Job.DoesNotExist:
        return status.HTTP_404_NOT_FOUND, {'error': 'Job not found'}


@job_router.delete('/{job_id}',auth=CompanyAuth())
def delete_job(request, job_id: UUID4):
    try:
        job = Job.objects.get(id=job_id)
        job.delete()
    except Job.DoesNotExist:
        return {'message': 'job does not exist'}
    return {'message': 'job deleted successfully'}


@job_router.delete('/',auth=CompanyAuth())
def delete_all_jobs(request):
    Job.objects.all().delete()
    return {'message': 'all jobs deleted successfully'}


@job_router.post('/', response={
    201: JobCreationSchema,
    400: FourOFour, }, auth=CompanyAuth())
def create_job(request, job: JobCreationSchema):
    try:
        qs = Job.objects.create(**job.dict())
        print("created")
        return status.HTTP_201_CREATED, qs
    except:
        return status.HTTP_400_BAD_REQUEST, {'error': 'something went wrong'}


@job_router.put('/{job_id}', response={
    200: JobUpdateOut,
    400: FourOFour, }, auth=CompanyAuth())
def update_job(request, job_in: JobUpdateOut, job_id: UUID4):
    try:
        job = get_object_or_404(Job, id=job_id)
        job.position = job_in.position
        job.employment_type = job_in.employment_type
        job.description = job_in.description
        job.location = job_in.location
        job.workplace = job_in.workplace
        job.save()
        return job

    except:
        return status.HTTP_400_BAD_REQUEST, {'error': 'something went wrong'}


@job_router.get('get_jobs_by_company/{company_id}', response={200: List[JobSchema], 400: FourOFour})
@paginate
def get_jobs_by_company(request, company_id: UUID4):
    try:
        jobs = Job.objects.filter(
            company_id=company_id).order_by("-created").all()
        return jobs
    except:
        return status.HTTP_400_BAD_REQUEST, {'error': 'something went wrong'}
