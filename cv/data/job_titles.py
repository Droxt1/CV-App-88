from django.db import models


class JobTitle(models.TextChoices):
    MARKETING_SPECIALIST = 'MARKETING SPECIALIST', 'Marketing Specialist'
    MARKETING_MANAGER = 'MARKETING MANAGER', 'Marketing manager'
    MARKETING_DIRECTOR = 'MARKETING DIRECTOR', 'Marketing Director'
    GRAPHIC_DESIGNER = 'GRAPHIC DESIGNER', 'Graphic Designer'
    MARKETING_RESEARCH_ANALYST = 'MARKETING RESEARCH ANALYST', 'Marketing Research Analyst'
    MARKETING_COMMUNICATIONS_MANAGER = 'MARKETING COMMUNICATIONS MANAGER', 'Marketing Communications Manager'
    MARKETING_CONSULTANT = 'MARKETING CONSULTAN', 'Marketing Consultant'
    PRODUCT_MANAGER = 'PRODUCT MANAGER', 'Product Manager'
    PUBLIC_RELATIONS = 'PUBLIC RELATIONS', 'Public Relations'
    SOCIAL_MEDIA_ASSISTANT = 'SOCIAL MEDIA ASSISTANT', 'Social Media Assistant'
    BRAND_MANAGER = 'BRAND MANAGER', 'Brand Manager'
    SEO_MANAGER = 'SEO MANAGER', 'Seo Manager'
    CONTENT_MARKETING_MANAGER = 'CONTENT MARKETING MANAGER', 'Content Marketing Manager'
    MEDIA_BUYER = 'MEDIA BUYER', 'Media Buyer'
    DIGITAL_MARKETING_MANAGER = 'DIGITAL MARKETING MANAGER', 'Digital Marketing Manager'
    ECOMMERCE_MARKETING_SPECIALIST = 'ECOMMERCE MARKETING SPECIALIST', 'Ecommerce Marketing Specialist'
    BRAND_STRATEGIST = 'BRAND STRATEGIST', 'Brand Strategist'
    MEDIA_RELATIONS_COORDINATOR = 'MEDIA RELATIONS COORDINATOR', 'Media Relations Coordinator'
    IT_PROFESSIONAL = 'IT PROFESSIONAL', 'IT Professional'
    UX_DESIGNER_and_UI_DEVELOPER = 'UX DESIGNER & UI DEVELOPER', 'UI Designer & UI Developer'
    SQL_DEVELOPER = 'SQL DEVELOPER', 'SQL Developer'
    WEB_DESIGNER = 'WEB DESIGNER', 'Web Designer'
    WEB_DEVELOPER = 'WEB DEVELOPER', 'Web Developer'
    HELP_DESK_WORKER_DESKTOP_SUPPORT = 'HELP DESK WORKER/DESKTOP SUPPORT', 'Help Desk Worker/desktop Support'
    SOFTWARE_ENGINEER = 'SOFTWARE ENGINEER', 'Software Engineer'
    DATA_ENTRY = 'DATA ENTRY', 'Data Entry'
    COMPUTER_PROGRAMMER = 'COMPUTER PROGRAMMER', 'Computer Programmer'
    NETWORK_ADMINISTRATOR = 'NETWORK ADMINISTRATOR', 'Network Administrator'
    INFORMATION_SECURITY_ANALYST = 'INFORMATION SECURITY ANALYST', 'Information Security Analyst'
    ARTIFICIAL_INTELLIGENCE_ENGINEER = 'ARTIFICIAL INTELLIGENCE ENGINEER', 'Artificial Intelligence Engineer'
    IT_MANAGER = 'IT MANAGER', 'IT Manager'
    TECHNICAL_SPECIALIST = 'TECHNICAL SPECIALIST', 'Technical Specialist'
    APPLICATION_DEVELOPER = 'APPLICATION DEVELOPER', 'Application Developer'
    BACKEND_DEVELOPER = 'BACKEND DEVELOPER', 'Backend Developer'
    FRONTEND_DEVELOPER = 'FRONTEND DEVELOPER', 'Frontend Developer'
    ADMINISTRATIVE_ASSISTANT = 'ADMINISTRATIVE ASSISTANT', 'Administrative Assistant'
    RECEPTIONIST = 'RECEPTIONIST', 'Receptionist'
    OFFICE_MANAGER = 'OFFICE MANAGER', 'Office Manager'
    AUDITING_CLERK = 'AUDITING CLERK', 'Auditing Clerk'
    BOOKKEEPER = 'BOOKKEEPER', 'Bookkeeper'
    ACCOUNT_EXECUTIVE = 'ACCOUNT EXECUTIVE', 'Account Executive'
    BRANCH_MANAGER = 'BRANCH MANAGER', 'Branch Manager'
    BUSINESS_MANAGER = 'BUSINESS MANAGER', 'Business Manager'
    QUALITY_CONTROL_COORDINATOR = 'QUALITY CONTROL COORDINATOR', 'Quality Control Coordinator'
    ADMINISTRATIVE_MANAGER = 'ADMINISTRATIVE MANAGER', 'Administrative Manager'
    HUMAN_RESOURCES = 'HUMAN RESOURCES', 'Human Resources'
    OFFICE_ASSISTANT = 'OFFICE ASSISTANT', 'Office Assistant'
    SECRETARY = 'SECRETARY', 'Secretary'
    ACCOUNT_COLLECTOR = 'ACCOUNT COLLECTOR', 'Account Collector'
