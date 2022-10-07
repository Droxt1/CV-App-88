from ninja import Router
from ninja.pagination import paginate

from cv.Auth.Authorization import CompanyAuth
from cv.models import JobApplication
from cv.schema import *

application_router = Router(tags=['application'])


@application_router.get('/', response=List[JobApplicationOut], auth=CompanyAuth())
@paginate
def get_all_jobs_applications(request):
    return JobApplication.objects.all().order_by('-created_at')


@application_router.get('/{job_application_id}', response=JobApplicationOut, auth=CompanyAuth())
def get_one_job_application(request, job_application_id: UUID4):
    return JobApplication.objects.get(id=job_application_id)


@application_router.delete('/{job_application_id}', auth=CompanyAuth())
def delete_job_application(request, job_application_id: UUID4):
    try:
        delt = JobApplication.objects.get(id=job_application_id)
        delt.delete()
    except JobApplication.DoesNotExist:
        return {'error': 'Job Application does not exist'}
    return {'success': 'Job Application deleted successfully'}
