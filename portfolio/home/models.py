from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.blocks import (
    StreamBlock,
)
from base.models import (
    HeadingBlock,
   CardBlock,
   CardsBlock,
)


class HomePageContent(StreamBlock):
    heading = HeadingBlock(
        help_text="Add a heading to the page."
    )
    cards = CardsBlock(
        help_text="Add a series of cards to the page."
    )

class HomePage(Page):
   profile_image = models.ForeignKey(
      'wagtailimages.Image',
      null=True,
      blank=True,
      on_delete=models.SET_NULL,
      related_name='+',
      help_text="Upload your profile image."
   )
   banner_header = models.CharField(
      max_length=255,
      blank=True,
      help_text="Text to display on the banner."
   )
   banner_subheader = models.TextField(
      blank=True,
      null=True,
      help_text="Subtext to display on the banner."
   )
   banner_cta_link_1 = models.ForeignKey(
      'wagtailcore.Page',
      null=True,
      blank=True,
      on_delete=models.SET_NULL,
      related_name='+',
      help_text="Link for the first call to action button."
   )
   banner_cta_link_2 = models.ForeignKey(
      'wagtailcore.Page',
      null=True,
      blank=True,
      on_delete=models.SET_NULL,
      related_name='+',
      help_text="Link for the first call to action button."
   )
   body = StreamField(
      HomePageContent(),
      blank=True,
      help_text="Add content to the body of the homepage."
   )
   content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                  FieldPanel('profile_image'),
                  FieldPanel('banner_header'),
                  FieldPanel('banner_subheader'),
                  FieldPanel('banner_cta_link_1'),
                  FieldPanel('banner_cta_link_2'),
                  
            ],
            heading="Banner section",
        ),
        FieldPanel('body'),
    ]
   

