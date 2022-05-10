import datetime
from django import forms
from django.contrib.auth import get_user_model

from .models import Doctor, TimeSlot

User = get_user_model()


class DoctorUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['first_name', 'middle_name',
                  'last_name', 'phone_no', 'address', 'qualification', 'experience', 'specialization', 'fees', 'timings', 'profile_image', 'certificate_image']


class TimeSlotForm(forms.ModelForm):
    class Meta:
        model = TimeSlot
        fields = ['day', 'start_time', 'end_time', 'half_time']
        widgets = {
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }


DAY_CHOICES = (('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'),
               ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'))


def get_today_day():
    today = datetime.datetime.now()
    return f'{today.strftime("%A")}'


class GetTimeSlotForm(forms.Form):
    days = forms.ChoiceField(choices=DAY_CHOICES, widget=forms.RadioSelect(
        attrs={'class': 'form-control'},
    ), initial=get_today_day
    )


class TimePickerInput(forms.TimeInput):
    input_type = 'time'


class EditTimeSlotForm(forms.ModelForm):
    class Meta:
        model = TimeSlot
        fields = ['day', 'start_time', 'end_time']
        widgets = {
            'day': forms.Select(attrs={'class': 'form-control'}),
            'start_time': TimePickerInput(
                attrs={'class': 'form-control'},
            ),
            'end_time': TimePickerInput(
                attrs={'class': 'form-control'},
            ),
        }


class AddTimeSlotForm(forms.Form):
    days = forms.MultipleChoiceField(choices=DAY_CHOICES, widget=forms.CheckboxSelectMultiple(

    ))
    start_time = forms.TimeField(
        widget=TimePickerInput(
            attrs={'class': 'form-control'},
        ))
    end_time = forms.TimeField(
        widget=TimePickerInput(
            attrs={'class': 'form-control'},
        ))


class EditDoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['first_name', 'middle_name',
                  'last_name', 'phone_no', 'address', 'qualification', 'experience', 'specialization', 'fees', 'timings', 'profile_image', 'certificate_image']
