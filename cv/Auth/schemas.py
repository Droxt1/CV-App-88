from ninja import Schema
from pydantic import EmailStr, Field, UUID4


class CustomerAuthIn(Schema):
    name: str = Field(..., example='John Doe')
    email: EmailStr
    phone: str = Field(..., example='07123456789',
                       min_length=11, max_length=11)
    password: str = Field(..., example='password', min_length=8, max_length=32)


class CustomerOut(Schema):
    id: UUID4
    name: str
    email: EmailStr
    phone: str

    class Config:
        orm_mode = True


class CompanyAuthIn(Schema):
    name: str
    phone: str = Field(..., example='07123456789',
                       max_length=11, min_length=11)
    email: EmailStr
    address: str = Field(..., example='Karada')
    country: str = Field(..., example='Iraq')
    password: str = Field(..., example='password', min_length=8, max_length=32)


class TokenOut(Schema):
    access: str


class CompanyOut(Schema):
    id: UUID4
    name: str
    phone: str
    email: EmailStr


class CompanyAuthOut(Schema):
    token: TokenOut
    company: CompanyOut


class CustomerAuthOut(Schema):
    token: TokenOut
    customer: CustomerOut


# class CompanyLoginIn(Schema):
#     email: EmailStr
#     password: str = Field(..., example='password', min_length=8, max_length=32)


# class CustomerLoginIn(Schema):
#     email: EmailStr
#     password: str = Field(..., example='password', min_length=8, max_length=32)

class Login(Schema):
    email: EmailStr 
    password: str = Field(..., example='password', min_length=8, max_length=32) 
class LoginOut(Schema):
    token: TokenOut
    id: UUID4 
    name: str
    email: EmailStr        