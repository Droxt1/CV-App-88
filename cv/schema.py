from ninja import Schema
from pydantic import UUID4
from typing import List


class CompanyOut(Schema):
    name: str = None
    description: str = None
    work_type: str
    city: str
    address: str = None
    image: str = None


class JobOut(Schema):
    uuid: UUID4
    company: CompanyOut
    position: str
    workplace: str
    location: str
    employment_type: str
    description: str


class CustomerOut(Schema):
    uuid: UUID4
    name: str
    phone: str
    description: str
    address: str
    skills: List[str]
    language: List[str]
    job_title: str
    image: str
    cv: str
    saved_job: List[JobOut]