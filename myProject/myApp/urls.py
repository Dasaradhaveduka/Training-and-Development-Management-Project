from django.urls import path
from .views import index_view, login_view, register_view, dashboard_view
from django import forms

urlpatterns = [
    path('', index_view, name='index'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('dashboard/', dashboard_view, name='dashboard'),
]
class TrainingNeedsAssessmentForm(forms.Form):
    feedback = forms.CharField(label='Feedback', widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}))
    courses = forms.MultipleChoiceField(choices=[
        ('Python Full Stack', 'Python Full Stack'),
        ('Java Full Stack', 'Java Full Stack'),
        ('Testing', 'Testing'),
        ('Data Science', 'Data Science'),
        # Add more courses as needed
    ], widget=forms.CheckboxSelectMultiple)
