# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import User, CompanyProfile,Customer , CustomerProfile, WorkExperience, Education, Job, JobApplication , Company


@admin.register(User)
class UserAdmin1(admin.ModelAdmin):
   list_display = ('id', 'name', 'email', 'password', )
   list_display_links = ('id', 'name', 'email', 'password', )
   search_fields = ('id', 'name', 'email', 'password', )
   list_filter = ('id', 'name', 'email', 'password', )



@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
   list_display = ('id', 'name', 'email', 'password', )
   list_display_links = ('id', 'name', 'email', 'password', )
   search_fields = ('id', 'name', 'email', 'password', )
   list_filter = ('id', 'name', 'email', 'password', )
   

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
   list_display = ('id', 'name', 'email', 'password', )
   list_display_links = ('id', 'name', 'email', 'password', )
   search_fields = ('id', 'name', 'email', 'password', )
   list_filter = ('id', 'name', 'email', 'password', )
   



@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'uuid',
        'created',
        'updated',
        'customer',
        'degree',
        'school', 
    )
    list_filter = ('created', 'updated', 'customer')


@admin.register(CompanyProfile)
class CompanyProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'uuid',
        'created',
        'updated',
        'name',
        'description',
        'work_type',
        'city',
        'address', 'image')
    
    list_filter = ('created', 'updated')




@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'uuid',
        'created',
        'updated',
        'customer',
        'title',
        'company_worked_for', 
    )
    list_filter = ('created', 'updated', 'customer')



@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    
    list_display = (
        'id',
        'uuid',
        'created',
        'updated',
        'name',
        'description',
        'address',
        'skills',
        'language',
        'job_title',  'cv')
    
    list_filter = ('created', 'updated')

    

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'uuid',
        'created',
        'updated',
        'company',
        'position',
        'workplace',
        'location',
        'employment_type',
        'description',
    )
    list_filter = ('created', 'updated', 'company')



@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'uuid',
        'created',
        'updated',
        'customer',
        'job',
        'category',
    )
    list_filter = ('created', 'updated', 'customer', 'job')
