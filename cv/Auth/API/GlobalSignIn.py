# build a global sign in page for both company and customer
import re
from django.db import IntegrityError
from ninja.errors import ValidationError
from rest_framework import status
from cv.models import Customer, Company
from cv.schema import FourOFour
from ninja import Router
from cv.Auth.Authorization import create_company_token, create_customer_token
from cv.Auth.schemas import *
from cv.models import Customer, Company
from cv.schema import FourOFour

sign_in_router = Router(tags=['global_sign_in'])


@sign_in_router.post("/login",
                     response={
                         200: LoginOut,

                         404: FourOFour,
                         500: FourOFour,
                         400: FourOFour, })
def login(request, payload: Login):
    try:
        company = Company.objects.get(email=payload.email)
        if company.password == payload.password:
            token = create_company_token(company)
            return 200, {
                'token': token,
                'id': company.id,
                'email': company.email,
                'name': company.name,

                
            }
        else:
            return status.HTTP_400_BAD_REQUEST, {'error': 'password is incorrect'}
    except Company.DoesNotExist:
        try:
            customer = Customer.objects.get(email=payload.email)
            if customer.password == payload.password:
                token = create_customer_token(customer)
                return 200, {
                    'token': token,
                    'id': customer.id,
                    'email': customer.email,
                    'name': customer.name,
                }
            else:
                return status.HTTP_400_BAD_REQUEST, {'error': 'password is incorrect'}
        except:
            return status.HTTP_404_NOT_FOUND, {'error': 'email does not exist'}
   

    # checking if the password is correct for both company and customer at the same time
    # try:
    #     try: company.password == payload.password:
    #         token = create_company_token(company)
    #         return 200, {
    #             'token': token,
    #             'company': company
    #         }
    #     except: customer.password == payload.password:
    #         token = create_company_token(customer)
    #         return 200, {
    #             'token': token,
    #             'customer': customer
    #         }
    # except IntegrityError:
    #     return status.HTTP_500_INTERNAL_SERVER_ERROR, {'error': 'internal server error, maybe email validation error'}
    # except:
    #         return status.HTTP_400_BAD_REQUEST, {'error': 'password is incorrect'}
    # except IntegrityError:
    #     return status.HTTP_500_INTERNAL_SERVER_ERROR, {'error': 'internal server error, maybe email validation error'}
    # except ValidationError:
    #     return status.HTTP_400_BAD_REQUEST, {'error': 'something went wrong'}

    # try:
    #     if company.password == payloadCO.password:
    #         token = create_company_token(company)
    #         return 200, {
    #             'token': token,
    #             'company': company
    #         }
    #     else:
    #         return status.HTTP_400_BAD_REQUEST, {'error': 'password is incorrect'}
    # except IntegrityError:
    #     return status.HTTP_500_INTERNAL_SERVER_ERROR, {'error': 'internal server error, maybe email validation error'}
    # except ValidationError:
    #     return status.HTTP_400_BAD_REQUEST, {'error': 'password is incorrect'}
    # try:
    #     if customer.password == payloadCU.password:
    #         token = create_customer_token(customer)
    #         return 200, {
    #             'token': token,
    #             'customer': customer
    #         }
    #     else:
    #         return status.HTTP_400_BAD_REQUEST, {'error': 'password is incorrect'}
    # except IntegrityError:
    #     return status.HTTP_500_INTERNAL_SERVER_ERROR, {'error': 'internal server error, maybe email validation error'}
    # except ValidationError:
    #     return status.HTTP_400_BAD_REQUEST, {'error': 'password is incorrect'}
