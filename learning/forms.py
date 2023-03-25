from .models import Course, Review, Lesson
from django import forms
from django.forms.widgets import Textarea, TextInput
from django.forms.utils import ValidationError


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'authors', 'description', 'start_date', 'duration', 'price', 'count_lessons')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('content',)


class LessonForm(forms.ModelForm):
    course = forms.ModelChoiceField(queryset=Course.objects.all(), empty_label='Выберите курс', required=True,
                                    label='Курс', help_text='Укажите курс, к которому вы хотите добавить урок.')


    error_css_class = 'error_field'
    required_css_class = 'required_field'
    class Meta:
        model = Lesson
        fields = ('name', 'preview', 'course',)
        labels = {'name': '', 'preview': '', 'course': ''}
        widgets = {'name': TextInput(attrs={'placeholder': 'Введите название урока'}), 'preview': Textarea(attrs={
            'placeholder': 'Опишите содержимое урока',
            'rows': 20,
            'cols': 35,
        })}
        help_texts = {'preview': 'Описание не должно быть пустым.'}

    def clean_preview(self):
        preview_data = self.cleaned_data['preview']
        if len(preview_data) > 200:
            raise ValidationError('Слишком длинное описание. Максимум 200 символов.')


class OrderByAndSearchForm(forms.Form):

    PRICE_CHOICES = (
        ('title', 'По умолчанию'),
        ('price', 'Самые дешевые курсы'),
        ('-price', 'Самый дорогие курсы'),
    )

    search = forms.CharField(label='Поиск', label_suffix=':', required=False,
                             widget=TextInput(attrs={'placeholder': 'Введите запрос...'}))
    price_holder = forms.ChoiceField(label='', choices=PRICE_CHOICES, initial=PRICE_CHOICES[0])

class SettingsForm(forms.Form):
    paginate_by = forms.IntegerField(label='Запсией на одной странице', min_value=2, max_value=20, initial=5)