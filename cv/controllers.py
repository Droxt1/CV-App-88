from ninja import Router , File
from ninja.pagination import paginate, PageNumberPagination
from django.shortcuts import get_object_or_404
from cv.models import *
from typing import List
from cv.schema import *
from ninja.files import UploadedFile





job_router = Router(tags=['job'])
customer_router = Router(tags=['customer'])
company_router = Router(tags=['company'])


@job_router.get('/get_all_jobs', response=List[JobSchema])
def get_all_jobs(request):
    jobs = Job.objects.all()
    return jobs

@job_router.get('/get_one/{job_uuid}', response=JobSchema)
def get_one_job(request, job_uuid: UUID4):
    return Job.objects.get(id = job_uuid)


@job_router.delete('/delete_job/{job_uuid}')
def delete_job(request, job_uuid: UUID4):
    try:    
        job = Job.objects.get(id = job_uuid)
        job.delete()
    except Job.DoesNotExist:
        return {'message': 'job does not exist'}    
    return {'message': 'job deleted successfully'}

@job_router.delete('/delete_all_jobs')
def delete_all_jobs(request):
    Job.objects.all().delete()
    return {'message': 'all jobs deleted successfully'}


@customer_router.get('/get_all_customers', response=List[CustomerOut])
def gett(request,):
    return 200, CustomerProfile.objects.all()


@customer_router.get('/get_one_customer/{customer_uuid}' ,response=CustomerOut)
def det_one_customer(request, customer_id: UUID4):
    return CustomerProfile.objects.get(id = customer_id)

@customer_router.put('/update_customer/{customer_id}', response=CustomerProfileUpdate)
def update_customer(request, customer_id: UUID4, customer_in: CustomerProfileUpdate):
    customer = get_object_or_404(CustomerProfile, id=customer_id)
    customer.name = customer_in.name
    customer.phone = customer_in.phone
    customer.description = customer_in.description
    customer.address = customer_in.address
    customer.skills = customer_in.skills
    customer.language = customer_in.language
    customer.job_title = customer_in.job_title
    customer.save()
    return customer


@customer_router.post('/save_job/{customer_uuid}/{job_uuid}')
def save_job(request, customer_id: UUID4, job_id: UUID4):
    job = Job.objects.get(id = job_id)
    customer = CustomerProfile.objects.get(id = customer_id)
    return customer.saved_job.add(job)


@customer_router.delete('/delete_saved_job/{customer_id}/{job_id}')
def delete_saved_job(request, customer_id: UUID4, job_id: UUID4):
    job = Job.objects.get(id = job_id)
    customer = CustomerProfile.objects.get(id = customer_id)
    return customer.saved_job.remove(job)

@customer_router.get('/get_all_saved_jobs/{customer_uuid}', response=List[CustomerSavedJobOut])
def get_saved_jobs(request, customer_id: UUID4):
    customer = CustomerProfile.objects.get(id = customer_id)
    return customer.saved_job.all()

@customer_router.post('apply_for_job/{customer_uuid}/{job_uuid}', response=JobApplicationOut)
def apply_for_job(request, customer_id: UUID4, job_id: UUID4, why_apply: str):
    job = Job.objects.get(id = job_id)
    customer = CustomerProfile.objects.get(id = customer_id)
    return JobApplication.objects.create(job=job, customer=customer,why_apply=why_apply)

@customer_router.post('/upload_cv/{customer_uuid}', response=CustomerOut)
def upload_cv(request, customer_id: UUID4, cv: UploadedFile = File(...)):
    customer = CustomerProfile.objects.get(id = customer_id)
    customer.cv = cv
    customer.save()
    return customer

@customer_router.post('/upload_profile_pic/{customer_uuid}', response=CustomerImage)
def upload_profile_pic(request, customer_id: UUID4, profile_pic: UploadedFile = File(...)):
    customer = CustomerProfile.objects.get(id = customer_id)
    customer.image = profile_pic
    customer.save()
    return customer


@company_router.get('/get_one/{company_uuid}', response=CompanyOut)
def get_one_company(request, company_uuid: UUID4):
    return CompanyProfile.objects.get(id = company_uuid)


@company_router.post('/search_company/{company_name}', response=List[CompanyOut])
def search_company(request, company_name: str):
    return CompanyProfile.objects.filter(name__icontains = company_name)

@company_router.get('/get_all', response=List[CompanyOut])

def get_all_company(request):
    return 200, CompanyProfile.objects.all()

@company_router.put('/update_company/{company_id}', response=CompanyProfileUpdate)
def update_company(request, company_id: UUID4, company_in: CompanyProfileUpdate):
    company = get_object_or_404(CompanyProfile, id=company_id)
    company.name = company_in.name
    company.phone = company_in.phone
    company.description = company_in.description
    company.address = company_in.address
    company.save()
    return company
@company_router.post('/upload_logo/{company_uuid}', response=CompanyOut)
def upload_logo(request, company_id: UUID4, logo: UploadedFile = File(...)):
    company = CompanyProfile.objects.get(id = company_id)
    company.image = logo
    company.save()
    return company
@company_router.get('/get_all_job_applications/{company_uuid}', response=List[JobApplicationOut])
def get_all_job_applications(request, company_uuid: UUID4,job_uuid: UUID4):
    job = JobApplication.objects.get(id = job_uuid)
    return job.all()



@company_router.post('/create_job/{company_uuid}', response=JobCreationSchema)
def create_job(request,  job: JobCreationSchema):
    qs = Job.objects.create(**job.dict())
    print("created")
    return qs 

@company_router.get('/get_all_company_jobs/{company_uuid}', response=List[JobOut])
def get_all_company_jobs(request, company_id: UUID4):
    company = CompanyProfile.objects.get(id = company_id)
    return company.job.all()
    
@company_router.put('/update_job/{company_uuid}', response=JobUpdateOut)
def update_job(request, job_in: JobUpdateOut,job_id:UUID4):
    job = get_object_or_404(Job,id = job_id)
    job.position = job_in.position
    job.employment_type = job_in.employment_type
    job.description = job_in.description
    job.location = job_in.location
    job.workplace = job_in.workplace
    job.save()
    return job

@company_router.get('get_all_jobs_applications/', response=List[JobApplicationOut])
def get_all_jobs_applications(request):
    return JobApplication.objects.all()

@company_router.get('/get_one_job_application/{job_application_id}', response=JobApplicationOut)
def get_one_job_application(request, job_application_id: UUID4):
    return JobApplication.objects.get(id = job_application_id)

@company_router.delete('/delete_job_application/{job_application_id}', response=JobApplicationOut)
def delete_job_application(request, job_application_id: UUID4):
        delt = JobApplication.objects.get(id = job_application_id)
        delt.delete()
        return ('deleted')
   