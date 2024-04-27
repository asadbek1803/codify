from django.contrib import admin
from .models import SiteSettings, Team, Platforms, SiteUsersAbout, AboutUsQuestions
# Register your models here.
from django.contrib.admin import ModelAdmin

@admin.register(SiteSettings)
class SiteSettingsAdmin(ModelAdmin):
    list_display = ('id', 'little_title', 'big_title', 'description', 'video')
    list_filter = ('id', )
    search_fields = ('id', )


@admin.register(Team)
class TeamAdmin(ModelAdmin):
    list_display = ('id', 'full_name', 'work')
    search_fields = ('full_name', )


@admin.register(Platforms)
class PlatformsAdmin(ModelAdmin):
    list_display = ("id", 'name', 'image')
    search_fields = ('name', )

@admin.register(SiteUsersAbout)
class SiteUsersAbout(ModelAdmin):
    list_display = ('id', 'students', 'total_courses', 'finished_courses')
    search_fields = ('id', )

@admin.register(AboutUsQuestions)
class AboutUsQuestionAdmin(ModelAdmin):
    list_display = ('id', 'question', 'answer')
    search_fields = ('id', )
