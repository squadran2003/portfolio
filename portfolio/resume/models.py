from django.db import models
from wagtail.models import Page

# Create your models here.
class ResumePage(Page):
    """
    Model for the Resume page.
    This page will display the resume content.
    """
    template = "resume/resume_page.html"

    # Add any fields specific to the Resume page here
    # For example, you might want to add a field for the resume file or additional content

    content_panels = Page.content_panels + [
        # Add panels for any additional fields here
    ]

    subpage_types = []  # No subpages allowed for this page type
