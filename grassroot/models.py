from django.db import models
from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import (
    FieldPanel, FieldRowPanel,InlinePanel, MultiFieldPanel)
    
from wagtail.images.edit_handlers import ImageChooserPanel 
from wagtail.search import index
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.contrib.forms.edit_handlers import FormSubmissionsPanel



from django.utils.translation import gettext_lazy as _
from django.conf import settings


class RootPage(Page):    
    image0 = models.ImageField(upload_to='images/intro/%Y/%m/%d/',max_length=2000,blank=True ,null =True)
    body = RichTextField(blank=True)

    advert = models.ForeignKey(
        'home.Advert',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,related_name='+')

    header = models.ForeignKey(
        'home.Header',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,related_name='+')

    footer = models.ForeignKey(
        'home.Footer',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,related_name='+')        


    content_panels=Page.content_panels + [
        SnippetChooserPanel('advert'),
        SnippetChooserPanel('header'),
        SnippetChooserPanel('footer'),

        FieldPanel('body',classname = "full"),
        FieldPanel('image0'),




    ]

