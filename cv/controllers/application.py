from ninja import Router, File
from ninja.pagination import paginate, PageNumberPagination, RouterPaginated
from ninja.pagination import paginate, PageNumberPagination
from django.shortcuts import get_object_or_404
from cv.models import *
from typing import List
from cv.schema import *
from ninja.files import UploadedFile
from cv.data import *


application_router = RouterPaginated(tags=['application'])


@application_router.get('/', response=List[JobApplicationOut])
def get_all_jobs_applications(request):
    return JobApplication.objects.all()


@application_router.get('/{job_application_id}', response=JobApplicationOut)
def get_one_job_application(request, job_application_id: UUID4):
    return JobApplication.objects.get(id=job_application_id)


@application_router.delete('/{job_application_id}', response=JobApplicationOut)
def delete_job_application(request, job_application_id: UUID4):
    delt = JobApplication.objects.get(id=job_application_id)
    delt.delete()
    return ('deleted')
