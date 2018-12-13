import datetime

from django.db import models
from django.utils import timezone

from information.models import CourseDetail


class References(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Status(models.Model):
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.status


class Possibility(models.Model):
    possibility = models.CharField(max_length=100)

    def __str__(self):
        return self.possibility

    def get_progressbar(self):
        if self.possibility == '20%' or self.possibility == '10%':
            return "progress-bar-danger"
        elif self.possibility == '40%' or self.possibility == '30%':
            return "progress-bar-warning"
        elif self.possibility == '60%' or self.possibility == '50%':
            return ""
        elif self.possibility == '80%' or self.possibility == '70%':
            return "progress-bar-info"
        elif self.possibility == '100%' or self.possibility == '90%':
            return "progress-bar-success"


class Course(CourseDetail):

    def __str__(self):
        return self.name


class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    reference = models.ForeignKey(References, on_delete=models.CASCADE, related_name="enquries")
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name="enquries")
    possibility = models.ForeignKey(Possibility, null=True, blank=True, on_delete=models.SET_NULL,
                                    related_name="enquries")
    date = models.DateField(default=timezone.now)
    courses = models.ManyToManyField(Course, related_name="enquries")
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_followup_status(self):
        followups = self.followups.all()
        followup = next((x for x in followups if x.is_acknowledged == False), False)
        if (followup):
            return (datetime.date.today() >= followup.scheduled_date)


class FollowUp(models.Model):
    enquiry_id = models.ForeignKey(Enquiry, on_delete=models.CASCADE, related_name="followups")
    scheduled_time = models.TimeField(blank=True, )
    scheduled_date = models.DateField(blank=True, )
    is_acknowledged = models.BooleanField(default=False)
    remarks = models.TextField(blank=True, null=True)

    def validate_date_time(self):
        return (datetime.date.today() <= self.scheduled_date)
