from django.db import models

# Create your models here.
from django.db import models
from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel ,InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel 
from wagtail.search import index
from django.utils.translation import gettext_lazy as _


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
    image = models.ImageField(upload_to='images/%Y/%m/%d/',max_length=2000,blank=True ,null =True)
    title0 = models.CharField(max_length=200, blank=True,null=True)
    title1 = models.CharField(max_length=200, blank=True,null=True)
    stars = models.IntegerField(default=5)

    content_panels=Page.content_panels + [
        FieldPanel('intro',classname = "full"),
        FieldPanel('image'),
        FieldPanel('title0'),
        FieldPanel('title1'),
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