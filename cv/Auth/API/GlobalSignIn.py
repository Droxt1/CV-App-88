from django.db import IntegrityError
from ninja import Router
from ninja.errors import ValidationError
from rest_framework import status
from cv.Auth.Authorization import create_company_token, create_customer_token
from cv.Auth.schemas import *
from cv.models import Customer, Company, CompanyStatus
from cv.schema import FourOFour

sign_in_router = Router(tags=['global_sign_in'])


@sign_in_router.post("/login",
                     response={
                         200: LoginOut,
                         404: FourOFour,
                         500: FourOFour,
                         400: FourOFour, })
def login(request, payload: LoginWithPhoneOrEmail):
    try:
        try:
            company_email = Company.objects.get(email=payload.email_or_phone)
            if company_email.password == payload.password:


                if company_email.status == CompanyStatus.PENDING:
                    return status.HTTP_400_BAD_REQUEST, {'error': 'Company is not approved yet, please wait for approval'}




                else:

                    token = create_company_token(company_email)
                    return status.HTTP_200_OK, {
                        'token': token,
                        'role': 'company',
                        'status': company_email.status,
                        'id': company_email.id,
                        'name': company_email.name,
                        'email': company_email.email,
                        'phone': company_email.phone,
                    }
            else:
                return status.HTTP_400_BAD_REQUEST, {'error': 'password is incorrect'}
        except:
            company_phone = Company.objects.get(phone=payload.email_or_phone)
            if company_phone.password == payload.password:
                if company_phone.status == CompanyStatus.PENDING:
                    return status.HTTP_400_BAD_REQUEST, {'error': 'Company is not approved yet, please wait for approval'}

                else:
                    token = create_company_token(company_phone)
                    return status.HTTP_200_OK, {
                        'token': token,
                        'role': 'company',
                        'status': company_phone.status,
                        'id': company_phone.id,
                        'name': company_phone.name,
                        'email': company_phone.email,
                        'phone': company_phone.phone,
                    }
            else:
                return status.HTTP_400_BAD_REQUEST, {'error': 'password is incorrect'}
    except Company.DoesNotExist:
        try:
            try:
                customer_email = Customer.objects.get(email=payload.email_or_phone)
                if customer_email.password == payload.password:
                    if customer_email.status == CompanyStatus.PENDING:
                        return status.HTTP_400_BAD_REQUEST, {'error': 'Customer is not approved yet, please wait for approval'}
                    else:
                        token = create_customer_token(customer_email)
                        return status.HTTP_200_OK, {
                            'token': token,
                            'role': 'customer',
                            'status': customer_email.status,
                            'id': customer_email.id,
                            'name': customer_email.name,
                            'email': customer_email.email,
                            'phone': customer_email.phone,
                        }
                else:
                    return status.HTTP_400_BAD_REQUEST, {'error': 'password is incorrect'}
            except:
                customer_phone = Customer.objects.get(phone=payload.email_or_phone)
                if customer_phone.password == payload.password:
                    if customer_phone.status == CompanyStatus.PENDING:
                        return status.HTTP_400_BAD_REQUEST, {'error': 'Customer is not approved yet, please wait for approval'}
                    else:
                        token = create_customer_token(customer_phone)
                        return status.HTTP_200_OK, {
                            'token': token,
                            'role': 'customer',
                            'status': customer_phone.status,
                            'id': customer_phone.id,
                            'name': customer_phone.name,
                            'email': customer_phone.email,
                            'phone': customer_phone.phone,
                        }
                else:
                    return status.HTTP_400_BAD_REQUEST, {'error': 'password is incorrect'}
        except Customer.DoesNotExist:
            return status.HTTP_404_NOT_FOUND, {'error': 'email or phone number does not exist'}
        except IntegrityError:
            return status.HTTP_500_INTERNAL_SERVER_ERROR, {'error': 'internal server error, maybe email validation error'}
        except ValidationError:
            return status.HTTP_400_BAD_REQUEST, {'error': 'something went wrong'}


