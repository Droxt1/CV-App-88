from ninja import Router
from django.shortcuts import get_object_or_404
from cv.models import *
from typing import List
from cv.schema import *

job_router = Router(tags=['job'])
customer_router = Router(tags=['customer'])


@job_router.get('/get_all', response=List[JobOut])
def get_all(request):
    return 200, Job.objects.all()


@job_router.get('/get_one/{job_uuid}', response=JobOut)
def get_one_job(request, job_uuid: UUID4):
    return Job.objects.get(uuid = job_uuid)


@job_router.delete('/delete_job/{job_uuid}')
def delete_job(request, job_uuid: UUID4):
    job = Job.objects.get(uuid = job_uuid)
    return job.delete()


@customer_router.get('/get_all_suers', response=List[CustomerOut])
def gett(request,):
    return 200, CustomerProfile.objects.all()


@customer_router.get('/get_one_customer/{customer_uuid}', response=CustomerOut)
def det_one_customer(request, customer_uuid: UUID4):
    return CustomerProfile.objects.get(uuid = customer_uuid)


@customer_router.post('/save_job/{customer_uuid}/{job_uuid}')
def save_job(request, customer_uuid: UUID4, job_uuid: UUID4):
    job = Job.objects.get(uuid = job_uuid)
    customer = CustomerProfile.objects.get(uuid = customer_uuid)
    return customer.saved_job.add(job)


@customer_router.delete('/delete_save_job/{customer_uuid}/{job_uuid}')
def delete_save_job(request, customer_uuid: UUID4, job_uuid: UUID4):
    job = Job.objects.get(uuid = job_uuid)
    customer = CustomerProfile.objects.get(uuid = customer_uuid)
    return customer.saved_job.remove(job)