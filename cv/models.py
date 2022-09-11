from datetime import datetime
from email.mime import image
from unicodedata import name
import uuid as uuid
from django.db import models
from multiselectfield import MultiSelectField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
import datetime



class Category(models.TextChoices):
    LONG_LIST = 'LONG_LIST', 'Long List'
    SHORT_LIST = 'SHORT LIST', 'Short List'



class CompanyWorkType(models.TextChoices):
    BACKEND = 'BACKEND', 'Backend'
    FRONTEND = 'FRONTEND', 'Frontend'


Skills =     (('item_key1', 'Item title 1.1'),
              ('item_key2', 'Item title 1.2'),
              ('item_key3', 'Item title 1.3'),
              ('item_key4', 'Item title 1.4'),
              ('item_key5', 'Item title 1.5'))


class JobTitle(models.TextChoices):
    BACKEND = 'BACKEND', 'Backend'
    FRONTEND = 'FRONTEND', 'Frontend'


class JobPosition(models.TextChoices):
    BACKEND = 'BACKEND', 'Backend'
    FRONTEND = 'FRONTEND', 'Frontend'


class EmploymentType(models.TextChoices):
    FULL_TIME = 'FULL TIME', 'Full time'
    PART_TIME = 'PART TIME', 'Part time'


class WorkplaceType(models.TextChoices):
    ON_SITE = 'ON SITE', 'on site'
    REMONTE = 'REMONTE', 'Remonte'


class JobLocation(models.TextChoices):
    BAGHDAD = 'BAGHDAD', 'Baghdad'
    BASRA = 'BASRA', 'Basra'


Language = (('item_key1', 'Item title 1.1'),
              ('item_key2', 'Item title 1.2'),
              ('item_key3', 'Item title 1.3'),
              ('item_key4', 'Item title 1.4'),
              ('item_key5', 'Item title 1.5'))










"""
class CutomerManger(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    def get_queryset(self):
        return super().get_queryset().filter(role=User.Role.CUSTOMER)

class Costumer(User):
    objects = CutomerManger()
    class Meta:
        proxy = True
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'


class CustomerUser(User):
    base_role = User.Role.CUSTOMER
    class Meta:
        proxy = True

@receiver(post_save, sender=CustomerUser)
def create_customer_profile(sender, instance, created, **kwargs):
        if created and instance.role == User.Role.CUSTOMER:
            CustomerUser.objects.create(user=instance)
        CustomerUser.objects.create(user=instance)
    
    

class CompanyManger(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Company must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    def get_queryset(self):
        return super().get_queryset().filter(role=User.Role.COMPANY)

class CompanyUser(User):
    base_role = User.Role.COMPANY
    class Meta:
        proxy = True     




class User(AbstractUser):
    class Role(models.TextChoices):
        COMPANY = 'COMPANY', 'Company'
        CUSTOMER = 'CUSTOMER', 'Customer'
        ADMIN = 'admin', 'Admin'

    base_role = Role.ADMIN
    role = models.CharField(max_length=50, choices=Role.choices, default=base_role)
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
        super().save(*args, **kwargs) 
"""
class Profile(models.Model):

    class Meta:
        abstract = True

  
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(editable=False, auto_now_add=True)
    updated = models.DateTimeField(editable=False, auto_now=True)


class CompanyUser(Profile):
  
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)


class UserProfile(Profile):
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    

class CompanyProfile(Profile):
    Name = models.CharField(max_length=50, unique=True, null=True, blank=True,default='Company Name')
    description = models.TextField(null=True, blank=True)
    work_type = models.CharField(choices=JobTitle.choices, max_length=20)
    city = models.CharField(choices=JobLocation.choices, max_length=20)
    address = models.CharField(max_length=255, null=True, blank=True)
    CompanyProfileImage = models.ImageField(upload_to='company_profile/', null=True, blank=True, default='company_profile/default.png')



class CustomerProfile(Profile):
    Name = models.CharField(max_length=50, unique=True, null=True, blank=True, default='Customer')
    description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    skills = MultiSelectField(choices=Skills, max_choices=3, max_length=255)
    language = MultiSelectField(choices=Language, max_choices=4, max_length=255)
    job_title = models.CharField(choices=JobTitle.choices, max_length=30)
    UserProfileImage = models.ImageField(upload_to='customer_profile/', null=True, blank=True, default='default.jpg')
    Cv = models.FileField(upload_to='customer_profile/', null=True, blank=True,default='default.pdf')
    


class WorkExperience(Profile):
    customer = models.ForeignKey(CustomerProfile, related_name='work_experience', on_delete=models.CASCADE)
    title = models.CharField(choices=JobTitle.choices, max_length=30)
    company_worked_for = models.CharField(max_length=50, null=False, blank=False)
    start_date = models.DateField(null=True, blank=True, default=datetime.date.today)
    end_date = models.DateField(null=True, blank=True, default=None)



class Education(Profile):
    customer = models.ForeignKey('CustomerProfile', related_name='education', on_delete=models.CASCADE)
    degree = models.CharField(max_length=255, null=True, blank=True)
    school = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True, default=datetime.date.today)
    end_date = models.DateField(null=True, blank=True, default=None)



class Job(Profile):
    company = models.ForeignKey(CompanyProfile, related_name='job', on_delete=models.CASCADE)
    position = models.CharField(choices=JobTitle.choices, max_length=30)
    workplace = models.CharField(choices=WorkplaceType.choices, max_length=30)
    location = models.CharField(choices=JobLocation.choices,max_length=40)
    employment_type = models.CharField(choices=EmploymentType.choices, max_length=30)
    description = models.TextField(null=True, blank=True)
    saved_by = models.ForeignKey(CustomerProfile, related_name='job', null=True, blank=True, on_delete=models.SET_NULL)
    JobImage = models.ImageField(upload_to='job/', null=True, blank=True, default='default.jpg', verbose_name='Job Image')
    

    


class JobApplication(Profile):
    customer = models.ForeignKey(CustomerProfile, related_name='job_application', on_delete=models.CASCADE, null=True, blank=True)
    job = models.ForeignKey(Job, related_name='job_application', on_delete=models.CASCADE, null=True, blank=True)
    category = models.CharField(choices=Category.choices, max_length=30,default=Category.LONG_LIST)

    
