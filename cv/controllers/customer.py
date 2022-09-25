from ninja import Router , File , UploadedFile
from ninja.pagination import paginate, PageNumberPagination ,RouterPaginated
from ninja.pagination import paginate, PageNumberPagination
from django.shortcuts import get_object_or_404
from cv.models import *
from typing import List
from cv.schema import *
from ninja.files import UploadedFile
from cv.data import *

customer_router = Router(tags=['customer'])





@customer_router.get('/skills', response=List[SkillOut])
def get_all_skills(request):
    result = []
    for i in Skills:
            result.append({
                'skills': i[0]
             })
    return result

@customer_router.get('/cities', response=List[CityOut])
def City_Out(request):
    result = []
    for i in JobLocation:
            result.append({
                'city': i[1]
                
            })
    return result

@customer_router.get('/job_titles', response=List[JobTout])
def Job_title_Out(request):
    result = []
    for i in JobTitle:
            result.append({
                'job_title': i[1]
                
            })
    return result

   








@customer_router.get('/', response=List[CustomerOut])
def get_all_customers(request):

   profiles = CustomerProfile.objects.all()
   return profiles


@customer_router.get('/{customer_id}' ,response=CustomerOut)
def det_one_customer(request, customer_id: UUID4):
    return CustomerProfile.objects.get(id = customer_id)

@customer_router.put('/{customer_id}', response=CustomerProfileUpdate)
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


@customer_router.post('/{customer_id}{job_id}')
def save_job(request, customer_id: UUID4, job_id: UUID4):
    job = Job.objects.get(id = job_id)
    customer = CustomerProfile.objects.get(id = customer_id)
    return customer.saved_job.add(job)


@customer_router.delete('/{customer_id}{job_id}')
def delete_saved_job(request, customer_id: UUID4, job_id: UUID4):
    job = Job.objects.get(id = job_id)
    customer = CustomerProfile.objects.get(id = customer_id)
    return customer.saved_job.remove(job)

@customer_router.get('/get_all_saved_jobs/{customer_id}', response=List[CustomerSavedJobOut])
def get_saved_jobs(request, customer_id: UUID4):
    customer = CustomerProfile.objects.get(id = customer_id)
    return customer.saved_job.all()

@customer_router.post('apply_for_job/{customer_id}{job_id}', response=JobApplicationOut)
def apply_for_job(request, customer_id: UUID4, job_id: UUID4, why_apply: str):
    job = Job.objects.get(id = job_id)
    customer = CustomerProfile.objects.get(id = customer_id)
    return JobApplication.objects.create(job=job, customer=customer,why_apply=why_apply)



@customer_router.get('customer_work_experience/{customer_id}', response=List[WorkExperienceOut])
def customer_work_experience(request, customer_id: UUID4):
    customer = CustomerProfile.objects.get(id = customer_id)
    return customer.work_experience.all()

@customer_router.post('add_work_experience/{customer_id}', response=WorkExperienceOut)
def add_work_experience(request, customer_id: UUID4, work_experience_in: WorkExperienceIn):
    customer = CustomerProfile.objects.get(id = customer_id)
    return WorkExperience.objects.create(customer=customer, **work_experience_in.dict())
@customer_router.delete('/{customer_id}{work_experience_id}')
def delete_work_experience(request, customer_id: UUID4, work_experience_id: UUID4):
    work_experience = WorkExperience.objects.get(id = work_experience_id)
    work_experience.delete()
    return {'message': 'work experience deleted successfully'}
@customer_router.put('/{customer_id}{work_experience_id}', response=WorkExperienceOut)
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
@customer_router.delete('/{customer_id}/{education_id}')
def delete_education(request, customer_id: UUID4, education_id: UUID4):
    education = Education.objects.get(id = education_id)
    education.delete()
    return {'message': 'education deleted successfully'}
@customer_router.put('/{customer_id}{education_id}', response=EducationOut)
def update_education(request, customer_id: UUID4, education_id: UUID4, education_in: EducationIn):
    education = Education.objects.get(id = education_id)
    education.school = education_in.school
    education.degree = education_in.degree
    education.start_date = education_in.start_date
    education.end_date = education_in.end_date
 
    education.save()
    return education

@customer_router.post('/upload_cv/{customer_id}', response=CustomerOut)
def upload_cv(request, customer_id: UUID4, cv: UploadedFile = File(...)):
    customer = CustomerProfile.objects.get(id = customer_id)
    customer.cv = cv
    qs = customer.save()
    return qs  

@customer_router.post('/upload_profile_pic/{customer_id}', response=CustomerImage)
def upload_profile_pic(request, customer_id: UUID4, profile_pic: UploadedFile = File(...)):
    customer = CustomerProfile.objects.get(id = customer_id)
    customer.image = profile_pic
    customer.save()
    return customer    