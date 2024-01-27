from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Blog, BlogCategory, Appointment

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', "status", 'profile_picture', 'username', 'email', 'password1', 'password2', 'address_line1', 'city', 'state', 'pincode']

        def clean(self):
            cleaned_data = super().clean()
            password1 = cleaned_data.get("password1")
            password2 = cleaned_data.get("password2")

            if password1 and password2 and password1 != password2:
                raise forms.ValidationError("Passwords do not match. Please enter matching passwords.")

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'image', 'category', 'summary', 'content', 'is_draft']
        # widgets = {
        #     'category': forms.Select(choices=BlogCategory.objects.all())
        # }

class BlogCategoryForm(forms.ModelForm):
    class Meta:
        model = BlogCategory
        fields = ['name']

# class BlogForm(forms.ModelForm):
#     class Meta:
#         model = Blog
#         fields = ['title', 'image', 'category', 'summary', 'content', 'is_draft']
#     CATEGORY_CHOICES = [
#             ('Mental Health', 'Mental Health'),
#             ('Heart Disease', 'Heart Disease'),
#             ('Covid19', 'Covid19'),
#             ('Immunization', 'Immunization'),
#         ]

#     category = forms.ModelChoiceField(
#         queryset=BlogCategory.objects.all(),
#         empty_label="Select a category",
#         label='Category',
#         widget=forms.Select(attrs={'class': 'form-control'})
#     )

#     def __init__(self, *args, **kwargs):
#         super(BlogForm, self).__init__(*args, **kwargs)

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['speciality', 'date', 'start_time']