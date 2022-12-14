import uuid as uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField
from cv.data.cities import JobLocation
from cv.data.industry import Industry
from cv.data.job_titles import JobTitle
from cv.data.langs import Language
from cv.data.skills import Skills


class CompanyStatus(models.TextChoices):
    PENDING = 'PENDING', 'pending'
    APPROVED = 'APPROVED', 'approved'


class Category(models.TextChoices):
    LONG_LIST = 'LONG_LIST', 'Long List'
    SHORT_LIST = 'SHORT LIST', 'Short List'
    ALL = 'ALL', 'All'


class EmploymentType(models.TextChoices):
    FULL_TIME = 'FULL TIME', 'Full time'
    PART_TIME = 'PART TIME', 'Part time'


class WorkplaceType(models.TextChoices):
    ON_SITE = 'ON SITE', 'on site'
    REMOTE = 'REMOTE', 'Remote'
    HYBRID = 'HYBRID', 'Hybrid',


class CompanyType(models.TextChoices):
    eCommerce = 'eCommerce', 'eCommerce'
    TELECOM = 'TELECOM ', 'Telecom'
    NGO = 'NGO', 'NGO'
    MEDICAL = 'MEDICAL', 'Medical'
    FOOD_DELIVERY = 'FOOD DELIVERY', 'Food Delivery'


"""-------------------------------------------------------------------------------------------------------------------"""


class UserManager(BaseUserManager):

    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
    Custom user model where the email address is the unique identifier
    and has an is_admin field to allow access to the admin app
    """

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("The email must be set"))
        if not password:
            raise ValueError(_("The password must be set"))
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', 1)

        if extra_fields.get('role') != 1:
            raise ValueError('Superuser must have role of Global Admin')
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    class Role(models.TextChoices):
        COMPANY = 'COMPANY', 'COMPANY'
        CUSTOMER = 'CUSTOMER', 'CUSTOMER'
        ADMIN = 'ADMIN', 'ADMIN'

    base_role = Role.ADMIN
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    role = models.CharField(
        max_length=50, choices=Role.choices, default=base_role, editable=False)

    name = models.CharField(max_length=50, blank=True,
                            null=True, default='Name')
    email = models.EmailField(
        max_length=50, unique=True, null=True, blank=True)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)

    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role

        super().save(*args, **kwargs)


"""-------------------------------------------------------------------------------------------------------------------"""


class CustomerManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.CUSTOMER)


class Customer(User):
    phone = models.CharField(max_length=50, blank=True,
                             null=True, default='Phone')
    status = models.CharField(max_length=50, choices=CompanyStatus.choices, default=CompanyStatus.APPROVED)
    base_role = User.Role.CUSTOMER

    Customer = CustomerManager()

    class meta:
        unique_together = ('email', 'phone')


"""-------------------------------------------------------------------------------------------------------------------"""

"""*******************************************************************************************************************"""


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


class Company(User):
    phone = models.CharField(max_length=50, blank=True,
                             null=True, default='Phone')
    status = models.CharField(max_length=50, choices=CompanyStatus.choices, default=CompanyStatus.PENDING)

    country = models.CharField(
        max_length=50, null=True, blank=True, default='Iraq')

    base_role = User.Role.COMPANY
    Company = CompanyManger()


"""*******************************************************************************************************************"""


class Profile(models.Model):
    class Meta:
        abstract = True

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(editable=False, auto_now_add=True)
    updated_at = models.DateTimeField(editable=False, auto_now=True)
    is_active = models.BooleanField(default=True)


class Entity(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(editable=False, auto_now_add=True)
    updated_at = models.DateTimeField(editable=False, auto_now=True)
    is_active = models.BooleanField(default=True)


class CompanyProfile(Entity):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.OneToOneField(
        Company, on_delete=models.CASCADE, related_name='company_profile')
    phone = models.CharField(max_length=50, blank=True,
                             null=True, default='Phone', unique=True)
    email = models.EmailField(
        max_length=50, null=True, blank=True)
    password = models.CharField(
        max_length=32, blank=True, null=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    head_office = models.CharField(max_length=255, null=True, blank=True)
    founded = models.DateField(null=True, blank=True)
    work_type = models.CharField(choices=Industry, max_length=100)
    country = models.CharField(
        max_length=50, null=True, blank=True, default='Iraq')
    city = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='company/', null=True,
                              blank=True, )

    def __str__(self):
        return self.name


@receiver(post_save, sender=Company)
def create_user_profile(sender, instance, created, **kwargs):
    try:
        CompanyProfile.objects.get(user=instance, name=instance.name, email=instance.email, country=instance.country,
                                   phone=instance.phone, password=instance.password,
                                   id=instance.id, )
    except CompanyProfile.DoesNotExist:
        if created and instance.role == "COMPANY":
            CompanyProfile.objects.create(user=instance, name=instance.name, email=instance.email,
                                          country=instance.country, phone=instance.phone, password=instance.password,
                                          id=instance.id, )
        else:
            instance.company_profile.save()


class Job(Profile):
    company = models.ForeignKey(
        CompanyProfile, related_name='job', on_delete=models.CASCADE)
    position = models.CharField(
        choices=JobTitle, max_length=100, blank=True, null=True)
    workplace = models.CharField(
        choices=WorkplaceType.choices, max_length=30, blank=True, null=True)
    location = models.CharField(
        choices=JobLocation, max_length=40, blank=True, null=True)
    employment_type = models.CharField(
        choices=EmploymentType.choices, max_length=30, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    expire_date = models.DateField(null=True, blank=True, auto_now_add=False)
    is_featured = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.position


class CustomerProfile(Entity):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.OneToOneField(
        Customer, on_delete=models.CASCADE, related_name='customer_profile')
    email = models.EmailField(max_length=50, null=True, blank=True)
    phone = models.CharField(null=True, blank=True, max_length=20, unique=True)
    password = models.CharField(null=True, blank=True, max_length=32)
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    skills = MultiSelectField(choices=Skills, max_choices=10, max_length=255)
    language = MultiSelectField(
        choices=Language, max_choices=10, max_length=255)
    job_title = models.CharField(choices=JobTitle, max_length=100)
    image = models.ImageField(upload_to='customer/',
                              null=True, blank=True, )
    cv = models.FileField(upload_to='CV/', null=True,
                          blank=True, )
    saved_job = models.ManyToManyField(Job, related_name='job', blank=True)

    def __str__(self):
        return self.name


@receiver(post_save, sender=Customer)
def create_user_profile(sender, instance, created, **kwargs):
    try:
        CustomerProfile.objects.get(
            user=instance, phone=instance.phone, email=instance.email, name=instance.name, id=instance.id)
    except CustomerProfile.DoesNotExist:
        if created and instance.role == "CUSTOMER":
            CustomerProfile.objects.create(
                user=instance, phone=instance.phone, email=instance.email, name=instance.name, id=instance.id)
        else:
            if instance.role == "CUSTOMER":
                instance.customer_profile.save()


class WorkExperience(Profile):
    customer = models.ForeignKey(
        CustomerProfile, related_name='work_experience', on_delete=models.CASCADE)
    title = models.CharField(choices=JobTitle, max_length=100)
    company_worked_for = models.CharField(
        max_length=50, null=False, blank=False)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True, default=None)


class Education(Profile):
    customer = models.ForeignKey(
        'CustomerProfile', related_name='education', on_delete=models.CASCADE)
    degree = models.CharField(max_length=255, null=True, blank=True)
    school = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True, )
    end_date = models.DateField(null=True, blank=True, )


class JobApplication(Profile):
    customer = models.ForeignKey(
        CustomerProfile, related_name='job_application', on_delete=models.CASCADE)
    job = models.ForeignKey(
        Job, related_name='job_application', on_delete=models.CASCADE)
    category = models.CharField(
        choices=Category.choices, max_length=30, default=Category.ALL)
    why_apply = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.job.position
