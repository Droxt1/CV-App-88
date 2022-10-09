from django.db import IntegrityError
from django.forms import ValidationError
from ninja import Router
from rest_framework import status
from cv.Auth.Authorization import create_company_token
from cv.Auth.schemas import *
from cv.models import Company
from cv.schema import FourOFour
company_auth_router = Router(tags=['company_auth'])


@company_auth_router.post('/company_signup', response={
    201: CompanyAuthOut,
    400: FourOFour,
    500: FourOFour,
    403: FourOFour,
})
def signup(request, payload: CompanyAuthIn):
    # if payload.password != payload.password:
    # return status.HTTP_400_BAD_REQUEST, {'error': 'passwords do not match'}

    if str(Company.objects.filter(phone=payload.phone).exists()) == 'True':
        return status.HTTP_400_BAD_REQUEST, {'error': 'email or phone number already exists'}
    else:
        try:
            new_company = Company.objects.create(
                name=payload.name,
                email=payload.email,
                phone=payload.phone,
                password=payload.password,
            )
            token = create_company_token(new_company)
            return status.HTTP_201_CREATED, {
                'token': token,
                'company': new_company
            }
        except IntegrityError:
            return status.HTTP_500_INTERNAL_SERVER_ERROR, {'error': 'internal server error, maybe email validation error'}
        except ValidationError:
            return status.HTTP_403_FORBIDDEN, {'error': 'something went wrong'}

