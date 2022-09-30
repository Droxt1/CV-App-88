from email.mime import application
from ninja import Router, File
from ninja.pagination import paginate
from django.shortcuts import get_object_or_404
from cv.models import *
from typing import List
from cv.schema import *
from ninja.files import UploadedFile
from cv.data import *


application_router = Router(tags=['application'])


@application_router.get('/', response=List[JobApplicationOut])
@paginate
def get_all_jobs_applications(request):
    return JobApplication.objects.all().order_by('-created')


@application_router.get('/{job_application_id}', response=JobApplicationOut)
def get_one_job_application(request, job_application_id: UUID4):
    return JobApplication.objects.get(id=job_application_id)


@application_router.delete('/{job_application_id}')
def delete_job_application(request, job_application_id: UUID4):
    try:
        delt = JobApplication.objects.get(id=job_application_id)
        delt.delete()
    except JobApplication.DoesNotExist:
        return {'error': 'Job Application does not exist'}
    return {'success': 'Job Application deleted successfully'}
