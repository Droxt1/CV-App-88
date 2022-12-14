from django.db import IntegrityError
from pydantic import ValidationError
from cv.models import Customer
from cv.schema import FourOFour
from cv.Auth.Authorization import create_customer_token
from cv.Auth.schemas import *
from ninja import Router
from rest_framework import status
customer_auth_router = Router(tags=['customer_auth'])


@customer_auth_router.post('/customer_signup', response={
    201: CustomerAuthOut,
    400: FourOFour,
    500: FourOFour,
    403: FourOFour,
})
def signup(request, payload: CustomerAuthIn):

    if str(Customer.objects.filter(phone=payload.phone).exists()) == 'True':
        return status.HTTP_400_BAD_REQUEST, {'error': 'email or phone number already exists'}
    else:
        try:
            new_customer = Customer.objects.create(
                name=payload.name,
                email=payload.email,
                phone=payload.phone,
                password=payload.password,
            )
            token = create_customer_token(new_customer)
            return status.HTTP_201_CREATED, {
                'token': token,
                'customer': new_customer
            }
        except IntegrityError:
            return status.HTTP_500_INTERNAL_SERVER_ERROR, {'error': 'internal server error, maybe email validation error'}
        except ValidationError:
            return status.HTTP_403_FORBIDDEN, {'error': 'something went wrong'}


