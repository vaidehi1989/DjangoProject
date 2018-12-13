from django.shortcuts import render, get_object_or_404

from enquiry.models import Enquiry


def enroll(request, pk):
    enquiry = get_object_or_404(Enquiry, pk=pk)
    return render("listEnquiries")
