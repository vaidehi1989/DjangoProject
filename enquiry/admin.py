from django.contrib import admin

from enquiry.models import References, Status, Enquiry, FollowUp, Course, Possibility

admin.site.register(References)
admin.site.register(Status)
admin.site.register(Course)
admin.site.register(Enquiry)
admin.site.register(FollowUp)
admin.site.register(Possibility)
