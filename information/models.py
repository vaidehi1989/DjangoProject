from django.core.files.storage import FileSystemStorage
from django.db import models


class CourseDetail(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(blank=True)
    syllabus = models.FileField(upload_to='static/media/course_content', blank=True)

    class Meta:
        abstract = True
