from django.contrib import admin
from .models import Course, Lesson

# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'start_date', 'duration')
    search_fields = ('title',)
    list_per_page = 3
    actions_on_top = True
    actions_on_bottom = True
    actions_selection_counter = True

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('course', 'name', 'preview')
    search_fields = ('name',)
    list_per_page = 3
    actions_on_top = True
    actions_on_bottom = True
    actions_selection_counter = True