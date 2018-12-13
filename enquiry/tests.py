import datetime

from enquiry.models import Enquiry

enquiry = Enquiry.objects.get(id=1)
followups = enquiry.followups.all()
followup = next((x for x in followups if x.is_acknowledged == False), False)

print(datetime.date.today() < followup.scheduled_date)