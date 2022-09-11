import uuid as uuid
from django.db import models
from multiselectfield import MultiSelectField
from mptt.models import MPTTModel, TreeForeignKey, TreeOneToOneField, TreeManyToManyField


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


class Profile(models.Model):
    class Meta:
        abstract = True

    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(editable=False, auto_now_add=True)
    updated = models.DateTimeField(editable=False, auto_now=True)


class CompanyUser(Profile):
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)


class User(Profile):
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100, unique=False, null=False, blank=False)


class CompanyProfile(Profile):
    company_user = models.OneToOneField(CompanyUser, related_name='company_profile', on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    work_type = models.CharField(choices=JobTitle.choices, max_length=20)
    city = models.CharField(choices=JobLocation.choices, max_length=20)
    address = models.CharField(max_length=255, null=True, blank=True)
    #image = models.ImageField('image', upload_to=)


class CustomerProfile(Profile):
    user = models.OneToOneField(User, related_name= 'customer_profile', on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    skills = MultiSelectField(choices=Skills, max_choices=3, max_length=255)
    language = MultiSelectField(choices=Language, max_choices=4, max_length=255)
    job_title = models.CharField(choices=JobTitle.choices, max_length=30)
    #image = models.ImageField
    #cv = models.FileField


class WorkExperience(Profile):
    customer = models.ForeignKey(CustomerProfile, related_name='work_experience', on_delete=models.CASCADE)
    title = models.CharField(choices=JobTitle.choices, max_length=30)
    company_worked_for = models.CharField(max_length=50, null=False, blank=False)
    #date =


class Education(Profile):
    customer = models.ForeignKey('CustomerProfile', related_name='education', on_delete=models.CASCADE)
    degree = models.CharField(max_length=255, null=True, blank=True)
    school = models.CharField(max_length=255, null=True, blank=True)
    #date =


class Job(Profile):
    company = models.ForeignKey(CompanyProfile, related_name='job', on_delete=models.CASCADE)
    postion = models.CharField(choices=JobTitle.choices, max_length=30)
    workplace = models.CharField(choices=WorkplaceType.choices, max_length=30)
    location = models.CharField(choices=JobLocation.choices,max_length=40)
    employment_type = models.CharField(choices=EmploymentType.choices, max_length=30)
    description = models.TextField(null=True, blank=True)
    saved_by = models.ManyToManyField(CustomerProfile, related_name='job', null=True, blank=True)


class JobApplication(Profile):
    customer = models.ForeignKey(CustomerProfile, related_name='job_application', on_delete=models.CASCADE, null=True, blank=True)
    job = models.ForeignKey(Job, related_name='job_application', on_delete=models.CASCADE, null=True, blank=True)
    category = models.CharField(choices=Category.choices, max_length=30)
