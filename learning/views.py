from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from datetime import datetime
from .forms import CourseForm
from django.urls import reverse
from .models import Course, Lesson, Tracking


# Create your views here.

class MainView(ListView):
    template_name = 'index.html'
    queryset = Course.objects.all()
    context_object_name = 'courses'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['current_year'] = datetime.now().year
        return context


class CourseCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'create.html'
    permission_required = ('learning.add_course',)

    def get_success_url(self):
        return reverse('detail', kwargs={'course_id': self.object.id})

    def form_valid(self, form):
        course = form.save(commit=False)
        course.save()
        return super(CourseCreateView, self).form_valid(form)


class CourseUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'create.html'
    pk_url_kwarg = 'course_id'
    permission_required = ('learning.change_course',)

    def get_queryset(self):
        return Course.objects.filter(id=self.kwargs.get('course_id'))

    def get_success_url(self):
        return reverse('detail', kwargs={'course_id': self.object.id})


class CourseDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Course
    template_name = 'delete.html'
    pk_url_kwarg = 'course_id'
    permission_required = ('learning.delete_course', )

    def get_queryset(self):
        return Course.objects.filter(id=self.kwargs.get('course_id'))

    def get_success_url(self):
        return reverse('index')


class CourseDetailView(DetailView):
    template_name = 'detail.html'
    context_object_name = 'course'
    pk_url_kwarg = 'course_id'

    def get_queryset(self):
        return Course.objects.filter(id=self.kwargs.get(CourseDetailView.pk_url_kwarg))

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['lessons'] = Lesson.objects.filter(course=self.kwargs.get(CourseDetailView.pk_url_kwarg))
        return context



@login_required
@permission_required('learning.add_tracking', raise_exception=True)
def enroll(request, course_id):
    if request.user.is_anonymous:
        return redirect('login')
    else:
        is_existed = Tracking.objects.filter(user=request.user).exists()
        if is_existed:
            return HttpResponse(f'???? ?????? ???????????????? ???? ???????? ????????')
        else:
            lessons = Lesson.objects.filter(course=course_id)
            records = [Tracking(lesson=lesson, user=request.user, passed=False) for lesson in lessons]
            Tracking.objects.bulk_create(records)
            return HttpResponse('???? ???????????????? ???? ???????????? ????????')
