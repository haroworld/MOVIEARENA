from dataclasses import field
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, ValidationError

from users.models import Profile

class RegistrationForm(UserCreationForm):

    error_messages = {
            "password_mismatch": ("The two password fields didn't match."),
        }

    class Meta:
        model = User
        fields = [
            'last_name','first_name','username','email','password1', 'password2'
        ]



    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch'
            )
        return password2

    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'w-full focus:outline-none'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Lastname'})
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Firstname'})
        self.fields['username'].widget.attrs.update({'placeholder': 'Username'})
        self.fields['username'].widget.attrs.update({'id': 'register-user'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
        self.fields['email'].widget.attrs.update({'id': 'register-email'})
        self.fields['email'].required = True
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password'})
        self.fields['password1'].widget.attrs.update({'id': 'reg-password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm Password'})
        self.fields['password2'].widget.attrs.update({'id': 'reg-password2'})

class EditprofileForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'last_name','first_name','username'
        ]


    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'w-full focus:outline-none'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'surname'})
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Firstname'})
        self.fields['username'].widget.attrs.update({'placeholder': 'Username'})
        self.fields['username'].widget.attrs.update({'id': 'register-user'})


class ChangeSettingsForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
            'profileType'
        ]

    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'w-full focus:outline-none'})


class ChangePicsForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
            'profile_image'
        ]

    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'w-full focus:outline-none'})

