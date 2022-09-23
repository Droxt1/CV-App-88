from ninja import Router , File
from ninja.pagination import paginate, PageNumberPagination
from ninja.pagination import RouterPaginated
from django.shortcuts import get_object_or_404
from cv.models import *
from typing import List
from cv.schema import *
from ninja.files import UploadedFile
from cv.data import *



job_router = RouterPaginated(tags=['job'])
customer_router = RouterPaginated(tags=['customer'])
company_router = RouterPaginated(tags=['company'])


@job_router.get('/get_all_jobs', response=List[JobSchema])
def get_all_jobs(request):
    jobs = Job.objects.all()
    return jobs

@job_router.get('/get_one/', response=JobSchema)
def get_one_job(request, job_uuid: UUID4):
    return Job.objects.get(id = job_uuid)


@job_router.delete('/delete_job/')
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


@customer_router.get('/get_all_skills', response=List[SkillOut])
def get_all_skills(request):
    result = []
    for i in Skills:
            result.append({
                'skills': i[0]
             })
    return result

@customer_router.get('/get_all_cities', response=List[CityOut])
def City_Out(request):
    result = []
    for i in JobLocation:
            result.append({
                'city': i[1]
                
            })
    return result

@customer_router.get('/get_all_job_titles', response=List[JobTout])
def Job_title_Out(request):
    result = []
    for i in JobTitle:
            result.append({
                'job_title': i[1]
                
            })
    return result

   








@customer_router.get('/get_all_customers', response=List[CustomerOut])
def gett(request):
    
    return 200, CustomerProfile.objects.all()


@customer_router.get('/get_one_customer/{customer_id}' ,response=CustomerOut)
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


@customer_router.post('/save_job/{customer_id}/{job_id}')
def save_job(request, customer_id: UUID4, job_id: UUID4):
    job = Job.objects.get(id = job_id)
    customer = CustomerProfile.objects.get(id = customer_id)
    return customer.saved_job.add(job)


@customer_router.delete('/delete_saved_job/{customer_id}/{job_id}')
def delete_saved_job(request, customer_id: UUID4, job_id: UUID4):
    job = Job.objects.get(id = job_id)
    customer = CustomerProfile.objects.get(id = customer_id)
    return customer.saved_job.remove(job)

@customer_router.get('/get_all_saved_jobs/{customer_id}', response=List[CustomerSavedJobOut])
def get_saved_jobs(request, customer_id: UUID4):
    customer = CustomerProfile.objects.get(id = customer_id)
    return customer.saved_job.all()

@customer_router.post('apply_for_job/{customer_id}/{job_id}', response=JobApplicationOut)
def apply_for_job(request, customer_id: UUID4, job_id: UUID4, why_apply: str):
    job = Job.objects.get(id = job_id)
    customer = CustomerProfile.objects.get(id = customer_id)
    return JobApplication.objects.create(job=job, customer=customer,why_apply=why_apply)

@customer_router.post('/upload_cv/{customer_id}', response=CustomerOut)
def upload_cv(request, customer_id: UUID4, cv: UploadedFile = File(...)):
    customer = CustomerProfile.objects.get(id = customer_id)
    customer.cv = cv
    customer.save()
    return customer

@customer_router.post('/upload_profile_pic/{customer_id}', response=CustomerImage)
def upload_profile_pic(request, customer_id: UUID4, profile_pic: UploadedFile = File(...)):
    customer = CustomerProfile.objects.get(id = customer_id)
    customer.image = profile_pic
    customer.save()
    return customer

@customer_router.get('customer_work_experience/{customer_id}', response=List[WorkExperienceOut])
def customer_work_experience(request, customer_id: UUID4):
    customer = CustomerProfile.objects.get(id = customer_id)
    return customer.work_experience.all()

@customer_router.post('add_work_experience/{customer_id}', response=WorkExperienceOut)
def add_work_experience(request, customer_id: UUID4, work_experience_in: WorkExperienceIn):
    customer = CustomerProfile.objects.get(id = customer_id)
    return WorkExperience.objects.create(customer=customer, **work_experience_in.dict())
@customer_router.delete('delete_work_experience/{customer_id}/{work_experience_id}')
def delete_work_experience(request, customer_id: UUID4, work_experience_id: UUID4):
    work_experience = WorkExperience.objects.get(id = work_experience_id)
    work_experience.delete()
    return {'message': 'work experience deleted successfully'}
@customer_router.put('update_work_experience/{customer_id}/{work_experience_id}', response=WorkExperienceOut)
def update_work_experience(request, customer_id: UUID4, work_experience_id: UUID4, work_experience_in: WorkExperienceIn):
    work_experience = WorkExperience.objects.get(id = work_experience_id)
    work_experience.company_worked_for = work_experience_in.company_worked_for
    work_experience.title = work_experience_in.title
    work_experience.start_date = work_experience_in.start_date
    work_experience.end_date = work_experience_in.end_date

    work_experience.save()
    return work_experience

@customer_router.get('customer_education/{customer_id}', response=List[EducationOut])
def customer_education(request, customer_id: UUID4):
    customer = CustomerProfile.objects.get(id = customer_id)
    return customer.education.all()
@customer_router.post('add_education/{customer_id}', response=EducationOut)
def add_education(request, customer_id: UUID4, education_in: EducationIn):
    customer = CustomerProfile.objects.get(id = customer_id)
    return Education.objects.create(customer=customer, **education_in.dict())
@customer_router.delete('delete_education/{customer_id}/{education_id}')
def delete_education(request, customer_id: UUID4, education_id: UUID4):
    education = Education.objects.get(id = education_id)
    education.delete()
    return {'message': 'education deleted successfully'}
@customer_router.put('update_education/{customer_id}/{education_id}', response=EducationOut)
def update_education(request, customer_id: UUID4, education_id: UUID4, education_in: EducationIn):
    education = Education.objects.get(id = education_id)
    education.school = education_in.school
    education.degree = education_in.degree
    education.start_date = education_in.start_date
    education.end_date = education_in.end_date
 
    education.save()
    return education










@company_router.get('/get_one/', response=CompanyOut)
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
    company.name = company_in.worked
    company.phone = company_in.phone
    company.description = company_in.description
    company.address = company_in.address
    company.save()
    return company
@company_router.post('/upload_logo/{company_id}', response=CompanyOut)
def upload_logo(request, company_id: UUID4, logo: UploadedFile = File(...)):
    company = CompanyProfile.objects.get(id = company_id)
    company.image = logo
    company.save()
    return company
@company_router.get('/get_all_job_applications/', response=List[JobApplicationOut])
def get_all_job_applications(request, company_uuid: UUID4,job_uuid: UUID4):
    job = JobApplication.objects.get(id = job_uuid)
    return job.all()



@company_router.post('/create_job/', response=JobCreationSchema)
def create_job(request,  job: JobCreationSchema):
    qs = Job.objects.create(**job.dict())
    print("created")
    return qs 

@company_router.get('/get_all_company_jobs/', response=List[JobOut])
def get_all_company_jobs(request, company_id: UUID4):
    company = CompanyProfile.objects.get(id = company_id)
    return company.job.all()
    
@company_router.put('/update_job/', response=JobUpdateOut)
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
