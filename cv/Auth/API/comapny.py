from ast import Delete
import email
from http.client import INTERNAL_SERVER_ERROR
from sys import prefix
from django.db import IntegrityError
from django.forms import ValidationError
from ninja import Router
from cv.Auth.Authorization import create_company_token, CompanyAuth
from cv.Auth.schemas import *
from cv.models import Company
from cv.schema import FourOFour
from rest_framework import status
from django.contrib.auth import authenticate
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
        # method do not pass the email after the second post request
        """def delete(self, request, *args, **kwargs):
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)"""
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

        """
        Company.objects.filter(email=payload.email)

        return status.HTTP_403_FORBIDDEN, {'error': 'email already exists'}
        
    except Company.DoesNotExist:
        
        company = Company.objects.create_user(name=payload.name,email=payload.email, 
        phone=payload.phone,address=payload.address, password=payload.password,country=payload.country)
        if company:
            token = create_company_token(company)
            return status.HTTP_201_CREATED, {
                'token': token,
                'company': company
            }
        else:
            return status.HTTP_500_INTERNAL_SERVER_ERROR, {'error': 'Internal Server Error'}
            """

    # this function delete new_company if it exists


# @company_auth_router.post('/company_login', response={
#     200: CompanyAuthOut,
#     404: FourOFour,
#     500: FourOFour,
#     400: FourOFour,
# })
# def login(request, payload: CompanyLoginIn):
#     try:
#         company = Company.objects.get(email=payload.email)
#     except Company.DoesNotExist:
#         return status.HTTP_404_NOT_FOUND, {'error': 'email does not exist'}

#     try:

#         if company.password == payload.password:
#             token = create_company_token(company)
#             return 200, {
#                 'token': token,
#                 'company': company
#             }
#         else:
#             return status.HTTP_400_BAD_REQUEST, {'error': 'password is incorrect'}
#     except IntegrityError:
#         return status.HTTP_500_INTERNAL_SERVER_ERROR, {'error': 'internal server error, maybe email validation error'}
#     except ValidationError:
#         return status.HTTP_400_BAD_REQUEST, {'error': 'password is incorrect'}

#     """
#     if company:
#         token = create_company_token(company)
#         return status.HTTP_200_OK, {
#             'token': token,
#             'company': company
#         }
#     else:
#         return status.HTTP_400_BAD_REQUEST, {'error': 'password is incorrect'}
#         """
"""
@company_auth_router.post('/company_login', response={
    200: CompanyAuthOut,
    404: FourOFour,
    500: FourOFour,
    400: FourOFour,
})
def login(request, payload: CompanyLoginIn):
    try:
        company = Company.objects.get(email=payload.email)
    except Company.DoesNotExist:
        return status.HTTP_404_NOT_FOUND, {'error': 'email does not exist'}

    try:

        if company.password == payload.password:
            token = create_company_token(company)
            return 200, {
                'token': token,
                'company': company
            }
        else:
            return status.HTTP_400_BAD_REQUEST, {'error': 'password is incorrect'}
    except IntegrityError:
        return status.HTTP_500_INTERNAL_SERVER_ERROR, {'error': 'internal server error, maybe email validation error'}
    except ValidationError:
        return status.HTTP_400_BAD_REQUEST, {'error': 'password is incorrect'}

    """
    if company:
        token = create_company_token(company)
        return status.HTTP_200_OK, {
            'token': token,
            'company': company
        }
    else:
        return status.HTTP_400_BAD_REQUEST, {'error': 'password is incorrect'}
        """
"""
