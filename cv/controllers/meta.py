from ninja import Router
from cv.data.cities import JobLocation
from cv.data.industry import Industry
from cv.data.job_titles import JobTitle
from cv.data.langs import Language
from cv.data.skills import Skills
from cv.schema import *

meta_router = Router(tags=['meta'])


@meta_router.get('/industries', response=List[IndustryOut])
def industries(request):
    result = []
    for i in Industry:
        result.append({
            'industry': i[1]
        })
    return result


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


@meta_router.get('/get_all_languages', response=List[LanguageOut])
def Language_Out(request):
    result = []
    for i in Language:
        result.append({
            'language': i[1]

        })
    return result
