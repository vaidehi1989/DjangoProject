import datetime

from django import forms
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput

from enquiry.models import Enquiry, Course, FollowUp, Status


class EnquiryForm(forms.ModelForm):
    courses = forms.ModelMultipleChoiceField(queryset=Course.objects.all())

    class Meta:
        model = Enquiry
        exclude = ('date', 'status')


class EditEnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ('name', 'phone', 'email', 'location', 'courses')


class ScheduleFollowupForm(forms.ModelForm):
    scheduled_time = forms.TimeField(widget=TimePickerInput(), label='Time')
    scheduled_date = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'), label='Date')
    schedule_form = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = FollowUp
        fields = ('scheduled_time', 'scheduled_date',)

class ACKForm(forms.ModelForm):
    ack_form = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = FollowUp
        fields = ('remarks',)


class StatusForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ('status', 'possibility')
