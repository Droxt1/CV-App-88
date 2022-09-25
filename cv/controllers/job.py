from ninja.pagination import RouterPaginated
from django.shortcuts import get_object_or_404
from cv.models import *
from typing import List
from cv.schema import *
from cv.data import *


job_router = RouterPaginated(tags=['job'])


@job_router.get('/', response=List[JobSchema])
def get_all_jobs(request):
    jobs = Job.objects.order_by("-created").all()
    return jobs


@job_router.get('/{job_id}', response=JobSchema)
def get_one_job(request, job_id: UUID4):
    return Job.objects.get(id=job_id)


@job_router.delete('/{job_id}')
def delete_job(request, job_id: UUID4):
    try:
        job = Job.objects.get(id=job_id)
        job.delete()
    except Job.DoesNotExist:
        return {'message': 'job does not exist'}
    return {'message': 'job deleted successfully'}


@job_router.delete('/')
def delete_all_jobs(request):
    Job.objects.all().delete()
    return {'message': 'all jobs deleted successfully'}


@job_router.post('/', response=JobCreationSchema)
def create_job(request,  job: JobCreationSchema):
    qs = Job.objects.create(**job.dict())
    print("created")
    return qs


@job_router.get('/{company_id}', response=List[JobOut])
def get_all_company_jobs(request, company_id: UUID4):
    company = CompanyProfile.objects.get(id=company_id)
    return company.job.all()


@job_router.put('/{job_id}', response=JobUpdateOut)
def update_job(request, job_in: JobUpdateOut, job_id: UUID4):
    job = get_object_or_404(Job, id=job_id)
    job.position = job_in.position
    job.employment_type = job_in.employment_type
    job.description = job_in.description
    job.location = job_in.location
    job.workplace = job_in.workplace
    job.save()
    return job