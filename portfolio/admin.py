from django.contrib import admin
from .models import PersonalInfo, Work, Paper, Project, Contact, Skill, Education


@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'title']


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_date', 'is_featured', 'order']
    list_filter = ['category', 'is_featured', 'created_date']
    search_fields = ['title', 'description']
    list_editable = ['is_featured', 'order']


@admin.register(Paper)
class PaperAdmin(admin.ModelAdmin):
    list_display = ['title', 'journal', 'publication_date', 'is_published', 'order']
    list_filter = ['is_published', 'publication_date', 'journal']
    search_fields = ['title', 'authors', 'journal']
    list_editable = ['is_published', 'order']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'is_ongoing', 'is_featured', 'order']
    list_filter = ['is_ongoing', 'is_featured', 'start_date']
    search_fields = ['name', 'description', 'technologies']
    list_editable = ['is_ongoing', 'is_featured', 'order']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['contact_type', 'value', 'is_primary', 'order']
    list_filter = ['contact_type', 'is_primary']
    search_fields = ['value']
    list_editable = ['is_primary', 'order']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'level', 'category', 'order']
    list_filter = ['category', 'level']
    search_fields = ['name']
    list_editable = ['level', 'order']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'school', 'start_year', 'is_current', 'order']
    list_filter = ['is_current', 'start_year']
    search_fields = ['degree', 'school', 'major']
    list_editable = ['is_current', 'order']