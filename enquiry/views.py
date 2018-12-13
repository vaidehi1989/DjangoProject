from django.shortcuts import render, redirect, get_object_or_404

from enquiry.forms import EditEnquiryForm, ScheduleFollowupForm, ACKForm, StatusForm
from enquiry.models import Status, FollowUp
from .models import Enquiry
from .forms import EnquiryForm


def listEnquiries(request):
    enquiries = Enquiry.objects.filter(status=Status.objects.get(id=1))

    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            enquiry = form.save(commit=False)
            enquiry.status = Status.objects.get(id=1)
            enquiry.save()
            form.save_m2m()
            return redirect('listEnquiries')
    else:
        form = EnquiryForm()
    return render(request, 'listenquries.html', {'enquiries': enquiries, 'form': form})


def enquiryEditView(request, pk):
    enquiry = get_object_or_404(Enquiry, pk=pk)
    if request.method == "POST":
        form = EditEnquiryForm(request.POST, instance=enquiry)
        if form.is_valid():
            enquiry = form.save(commit=False)
            enquiry.save()
            return redirect('listEnquiries', pk=enquiry.pk)
    else:
        form = EditEnquiryForm(instance=enquiry)
    return render(request, 'enquiryedit.html', {'form': form})


def followUpView(request, pk):
    enquiry = get_object_or_404(Enquiry, pk=pk)
    followups = enquiry.followups.all()
    followup = next((x for x in followups if x.is_acknowledged == False), False)
    form_status = StatusForm(instance=enquiry)
    if request.method == "POST":
        if 'schedule_form' in request.POST:
            form_schedule = ScheduleFollowupForm(request.POST)
            if form_schedule.is_valid():
                followup = form_schedule.save(commit=False)
                if followup.validate_date_time():
                    followup.enquiry_id = enquiry
                    followup.save()
                    return redirect('followupenquiry', pk=enquiry.pk)
                else:
                    form_schedule.add_error("scheduled_date", "Older date has been assigned")
                    return render(request, 'followups.html',
                                  {'followups': followups, 'form_schedule': form_schedule, 'form_ACK': ACKForm(),
                                   'enquiry': enquiry, 'form_status': form_status})

        elif 'ack_form' in request.POST:
            form_ACK = ACKForm(request.POST, instance=followup)
            if form_ACK.is_valid():
                followup = form_ACK.save(commit=False)
                followup.is_acknowledged = True
                followup.save()
                return redirect('followupenquiry', pk=enquiry.pk)
        else:
            form_status = StatusForm(request.POST, instance=enquiry)
            if form_status.is_valid():
                enq = form_status.save(commit=False)
                if enq.status.status == "enrolled":
                    return redirect('enroll', pk=enquiry.pk)
                enq.save()
                return redirect('listEnquiries')
    if followup:
        form_ACK = ACKForm(instance=followup)
        form_schedule = None
    else:
        form_schedule = ScheduleFollowupForm()
        form_ACK = None

    return render(request, 'followups.html',
                  {'followups': followups, 'form_schedule': form_schedule, 'form_ACK': form_ACK, 'enquiry': enquiry,
                   'form_status': form_status})
