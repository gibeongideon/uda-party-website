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


class County(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = _("County")
        verbose_name_plural = _("Counties")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("County_detail", kwargs={"pk": self.pk})


class Ward(models.Model):
    name = models.CharField(max_length=200)    

    class Meta:
        verbose_name = _("Ward")
        verbose_name_plural = _("Wards")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Ward_detail", kwargs={"pk": self.pk})


class CandidatePage(Page):
    intro = RichTextField(blank=True)
    # image = models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)
    image = models.ImageField(upload_to='images/candidate/%Y/%m/%d/',max_length=2000,blank=True ,null =True)
    image2 = models.ImageField(upload_to='images/candidate/%Y/%m/%d/',max_length=2000,blank=True ,null =True)
    title0 = models.CharField(max_length=200, blank=True,null=True)
    title1 = models.CharField(max_length=200, blank=True,null=True)
    stars = models.IntegerField(default=5)

    body_intro1 = models.CharField(max_length=200,default='Welcome dear<br /> friend!', blank=True,null=True)
    body = RichTextField(blank=True)

    word1 = models.CharField(max_length=200, blank=True,null=True)
    word2 = models.CharField(max_length=200, blank=True,null=True)
    word3 = models.CharField(max_length=200, blank=True,null=True)
    word4 = models.CharField(max_length=200, blank=True,null=True)
    word5 = models.CharField(max_length=200, blank=True,null=True)


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

        FieldPanel('intro',classname = "full"),
        FieldPanel('image'),
        FieldPanel('image2'),
        FieldPanel('title0'),
        FieldPanel('title1'),
        FieldPanel('word1'),
        FieldPanel('word2'),
        FieldPanel('word3'),
        FieldPanel('word4'),
        FieldPanel('word5'),
        
        InlinePanel('candidateiaes',label="Candidate Image")
    ]


class CandidateImage(Orderable):
    page = ParentalKey(CandidatePage, on_delete=models.CASCADE, related_name='candidateiaes')
    image = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE,related_name='+')
    caption = models.CharField(blank=True,max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]