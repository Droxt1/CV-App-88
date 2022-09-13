# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import User,UserProfile, CompanyProfile,Customer ,Company, CustomerProfile, WorkExperience, Education, Job, JobApplication 


@admin.register(User)
class UserAdmin1(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'role', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('role', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('id',)

@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'uuid', 'created', 'updated', 'parent', 'name')
    list_filter = ('created', 'updated', 'parent')
    search_fields = ('name',)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'role', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('role', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('id',)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'role', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('role', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('id',)



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
        'Name',
        'description',
        'work_type',
        'city',
        'address', 'CompanyProfileImage')
    
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
        'Name',
        'description',
        'address',
        'skills',
        'language',
        'job_title',  'Cv')
    
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
    raw_id_fields = ('saved_by',)


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
