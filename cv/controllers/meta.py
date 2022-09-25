from ninja import Router
from cv.models import *
from typing import List
from cv.schema import *
from cv.data import *


meta_router = Router(tags=['meta'])


@meta_router.get('/get_all_skills', response=List[SkillOut])
def get_all_skills(request):
    result = []
    for i in Skills:
        result.append({
            'skills': i[0]
        })
    return result


@meta_router.get('/get_all_cities', response=List[CityOut])
def City_Out(request):
    result = []
    for i in JobLocation:
        result.append({
            'city': i[1]

        })
    return result


@meta_router.get('/get_all_job_titles', response=List[JobTout])
def Job_title_Out(request):
    result = []
    for i in JobTitle:
        result.append({
            'job_title': i[1]

        })
    return result
