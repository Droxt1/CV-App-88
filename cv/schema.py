from datetime import datetime, date
from ninja import Schema, ModelSchema
from pydantic import UUID4
from typing import List
from cv.models import *
from datetime import datetime


class FourOFour(Schema):
    error: str

class two00_OK(Schema):
    message: str
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
    id: UUID4 = None
    name: str = None
    image: str = None


class JobOut(Schema):
    id: UUID4 = None
    company: CompanyJobOut = None
    position: str = None
    employment_type: str = None
    description: str = None
    location: str = None
    workplace: str = None


class WorkExperienceOut(Schema):
    id: UUID4 = None
    customer_id: UUID4 = None
    title: str = None
    company_worked_for: str = None
    start_date: date = None
    end_date: date = None


class WorkExperienceUpdateIn(Schema):
    id: UUID4 = None
    customer_id: UUID4 = None
    title: str = None
    company_worked_for: str = None
    start_date: date = None
    end_date: date = None


class WorkExperienceIn(Schema):
    customer_id: UUID4 = None
    title: str = None
    company_worked_for: str = None
    start_date: date
    end_date: date = None


class EducationOut(Schema):
    id: UUID4 = None
    customer_id: UUID4 = None
    school: str = None
    degree: str = None
    start_date: date = None
    end_date: date = None


class EducationIn(Schema):
    customer_id: UUID4 = None
    degree: str = None
    school: str = None
    start_date: date = None
    end_date: date = None


class EducationUpdateIn(Schema):
    id: UUID4 = None
    customer_id: UUID4 = None
    degree: str = None
    school: str = None
    start_date: date = None
    end_date: date = None


class CustomerOut(Schema):
    id: UUID4 = None
    name: str = None
    phone: str = None
    education: List[EducationOut] = None
    work_experience: List[WorkExperienceOut] = None
    description: str = None
    address: str = None
    skills: List[str] = None
    language: List[str] = None
    job_title: str = None
    image: str = None
    cv: str = None


class SkillOut(Schema):
    skills: str


class JobTout(Schema):
    job_title: str


class CityOut(Schema):
    city: str


class CustomerProfileUpdate(Schema):
    name: str = None
    phone: str = None
    description: str = None
    address: str = None
    skills: List[str] = None
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


class CustomerProfileUpdate(Schema):
    name: str = None
    phone: str = None
    description: str = None
    address: str = None
    skills: List[str] = None
    language: List[str] = None
    job_title: str = None


class CustomerProfileUpdateIn(Schema):
    name: str
    phone: str
    description: str
    address: str
    job_title: str
    skills: List[str]
    language: List[str]


class JobSchema(Schema):
    id: UUID4 = None
    company: CompanyJobOut = None
    created = datetime.now() 
    position: str = None
    employment_type: str = None
    description: str = None
    location: str = None
    workplace: str = None
    is_featured: bool = None
   


class JobSchemaOut(Schema):
    id: UUID4
    company: CompanyJobOut
    position: str = None
    employment_type: str = None
    description: str = None
    location: str = None
    workplace: str = None
    saved: bool = False


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
    


class JobApplicationIn(Schema):
    customer_id: UUID4 = None
    job_id: UUID4 = None
    why_apply: str = None


class JobUpdateOut(Schema):
    position: str = None
    employment_type: str = None
    description: str = None
    location: str = None
    workplace: str = None


class CustomerSavedJobOut(Schema):
    id: UUID4 = None
    company: CompanyJobOut = None
    position: str = None
    employment_type: str = None
    description: str = None
    location: str = None
    workplace: str = None


class CustomerImage(Schema):
    image: str = None


class CustomerId(Schema):
    customer_id: UUID4


class CV(Schema):
    cv: str


class CompanyID(Schema):
    company_id: UUID4


class CompanyImage(Schema):
    image: str


class WKID(Schema):
    work_experience_id: UUID4


class EDID(Schema):
    education_id: UUID4
