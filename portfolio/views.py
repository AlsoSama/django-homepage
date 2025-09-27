from django.shortcuts import render
from django.http import JsonResponse
from .models import PersonalInfo, Work, Paper, Project, Contact, Skill, Education


def home(request):
    """主页视图"""
    try:
        personal_info = PersonalInfo.objects.first()
    except PersonalInfo.DoesNotExist:
        personal_info = None
    
    featured_works = Work.objects.filter(is_featured=True)[:6]
    featured_projects = Project.objects.filter(is_featured=True)[:6]
    recent_papers = Paper.objects.filter(is_published=True)[:5]
    skills = Skill.objects.all()
    education = Education.objects.all()
    contacts = Contact.objects.all()
    
    # 处理项目技术栈分割
    for project in featured_projects:
        if project.technologies:
            project.tech_list = [tech.strip() for tech in project.technologies.split(',')]
        else:
            project.tech_list = []
    
    context = {
        'personal_info': personal_info,
        'featured_works': featured_works,
        'featured_projects': featured_projects,
        'recent_papers': recent_papers,
        'skills': skills,
        'education': education,
        'contacts': contacts,
    }
    
    return render(request, 'portfolio/home.html', context)


def works(request):
    """作品页面"""
    works = Work.objects.all()
    categories = Work.objects.values_list('category', flat=True).distinct()
    
    context = {
        'works': works,
        'categories': categories,
    }
    
    return render(request, 'portfolio/works.html', context)


def papers(request):
    """论文页面"""
    papers = Paper.objects.filter(is_published=True)
    
    context = {
        'papers': papers,
    }
    
    return render(request, 'portfolio/papers.html', context)


def projects(request):
    """项目页面"""
    projects = Project.objects.all()
    
    # 处理项目技术栈分割
    for project in projects:
        if project.technologies:
            project.tech_list = [tech.strip() for tech in project.technologies.split(',')]
        else:
            project.tech_list = []
    
    context = {
        'projects': projects,
    }
    
    return render(request, 'portfolio/projects.html', context)


def about(request):
    """关于页面"""
    try:
        personal_info = PersonalInfo.objects.first()
    except PersonalInfo.DoesNotExist:
        personal_info = None
    
    skills = Skill.objects.all()
    education = Education.objects.all()
    contacts = Contact.objects.all()
    
    context = {
        'personal_info': personal_info,
        'skills': skills,
        'education': education,
        'contacts': contacts,
    }
    
    return render(request, 'portfolio/about.html', context)


def contact(request):
    """联系页面"""
    contacts = Contact.objects.all()
    
    context = {
        'contacts': contacts,
    }
    
    return render(request, 'portfolio/contact.html', context)