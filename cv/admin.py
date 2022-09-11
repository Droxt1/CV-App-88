# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import CompanyUser, User, CompanyProfile, CustomerProfile, WorkExperience, Education, Job, JobApplication


@admin.register(CompanyUser)
class CompanyUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'uuid', 'created', 'updated', 'parent', 'name')
    list_filter = ('created', 'updated', 'parent')
    search_fields = ('name',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'uuid', 'created', 'updated', 'parent', 'name')
    list_filter = ('created', 'updated', 'parent')
    search_fields = ('name',)


@admin.register(CompanyProfile)
class CompanyProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'uuid',
        'created',
        'updated',
        'company_user',
        'description',
        'work_type',
        'city',
        'address',
    )
    list_filter = ('created', 'updated', 'company_user')


@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'uuid',
        'created',
        'updated',
        'user',
        'description',
        'address',
        'skills',
        'language',
        'job_title',
    )
    list_filter = ('created', 'updated', 'user')


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


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'uuid',
        'created',
        'updated',
        'company',
        'postion',
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
