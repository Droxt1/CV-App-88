from datetime import datetime
from email.mime import image
from urllib import response
import uuid
from ninja import Schema , ModelSchema
from pydantic import UUID4
from typing import List, Optional


from cv.models import Company, Job, CustomerProfile , CompanyProfile , JobApplication


class CompanyJOBOut(Schema):
    id: UUID4
    position: str = None
    employment_type: str = None
    description: str = None
    location: str = None
    workplace: str = None
    
    

class CompanyOut(Schema):
    id: UUID4 = None
    name: str = None
    email: str = None
    phone: str = None
    description: str = None
    work_type: str = None
    city: str = None
    address: str = None
    image: str = None
    job: List[CompanyJOBOut] = None
    
class CompanyProfileUpdate(Schema):
    name: str = None
    email: str = None
    phone: str = None
    description: str = None
    work_type: str = None
    city: str = None
    address: str = None
    image: str = None    
    
class CompanyJobOut(Schema):

    name: str = None
    image: str = None  
class JobOut(Schema):
    id: UUID4 = None
    position: str
    employment_type: str
    description: str
    location: str
    workplace: str


class WorkExperienceOut(Schema):
    title: str
    company_worked_for: str


class EducationOut(Schema):
    degree: str
    school: str


class CustomerOut(Schema):
    id: UUID4
    name: str
    phone: str
    education: List[EducationOut]
    work_experience: List[WorkExperienceOut]
    description: str
    address: str = None
    skills: List[str]
    language: List[str]
    job_title: str
    image: str = None
    cv: str = None
    saved_job: List[JobOut] = None


class CustomerProfileUpdate(Schema):
    name: str = None
    phone: str =None
    description: str = None
    address: str = None
    skills: List[str] =None
    language: List[str] = None
    job_title: str = None
    image: str = None
    cv: str = None   

class CustomerIn(Schema):
    name: str
    phone: str
    description: str
    address: str
    skills: List[str]
    language: List[str]
    job_title: str
    image: str
    cv: str

class JobIn(Schema):
    company: CompanyOut
    position: str
    employment_type: str
    description: str
    location: str
    workplace: str

class CompanyIn(Schema):
    name: str
    description: str
    work_type: str
    city: str
    address: str
    image: str
    

class JobUpdate(Schema):
    position: str
    workplace: str
    location: str
    employment_type: str
    description: str

class CompanyProfileUpdate(Schema):
    name: str = None
    phone: str = None
    description: str = None
    work_type: str = None
    city: str = None
    address: str = None
    image: str = None

class CustomerProfileUpdate(Schema):
    name: str
    phone: str
    description: str
    address: str
    skills: List[str]
    language: List[str]
    job_title: str
    image: str
    cv: str

class JobSchema(Schema):
    id: UUID4
    position: str = None
    employment_type: str = None
    description: str = None
    location: str = None
    workplace: str = None
    
class CompanyJobCreate(Schema):
    id: UUID4
class JobCreationSchema(Schema):

    company_id: UUID4 = None
    position: str = None
    employment_type: str = None
    description: str = None
    location: str = None
    workplace: str = None
    

    
class JobApplied(Schema):
    id: UUID4    
class CutomerAppliedJobsOut(Schema):
    id: UUID4
    name: str
    phone: str

class JobAppliedOut(Schema):
    id: UUID4 = None
    position: str = None
    workplace: str = None
    location: str = None
    employment_type: str = None
    
class CustomerApplyiedJobs(Schema):
    id: UUID4
    name: str
    job_title: str
    image: str

class JobApplicationOut(Schema):
    id: UUID4 = None
    customer: CustomerApplyiedJobs = None
    job: JobApplied = None
    why_apply: str = None
    


class JobUpdateOut(Schema):
    position: str = None
    employment_type: str = None
    description: str = None
    location: str = None
    workplace: str = None
    
class CustomerSavedJobOut(Schema):
    position: str
    employment_type: str
    description: str
    location: str
    workplace: str
    company: CompanyJobOut

class CustomerImage(Schema):
    image: str

class CompanyImage(Schema):
    image: str



