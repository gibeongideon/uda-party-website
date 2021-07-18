from django.db import models
from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel ,InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel 
from wagtail.search import index
from django.utils.translation import gettext_lazy as _


class HomePage(Page):
    faicon = models.ImageField(upload_to='images/faricon/%Y/%m/%d/',max_length=2000,blank=True ,null =True)
    image0 = models.ImageField(upload_to='images/intro/%Y/%m/%d/',max_length=2000,blank=True ,null =True)
    signature_01 = models.ImageField(upload_to='images/signature/%Y/%m/%d/',max_length=2000,blank=True ,null =True)
    logo = models.ImageField(upload_to='images/logo/%Y/%m/%d/',max_length=2000,blank=True ,null =True)
    logo1 = models.ImageField(upload_to='images/logo/%Y/%m/%d/',max_length=2000,blank=True ,null =True)

    logofooter = models.ImageField(upload_to='images/logo/%Y/%m/%d/',max_length=2000,blank=True ,null =True)

    intro_quote1 = models.CharField(default="Our quest to empower & change ",max_length=200, blank=True,null=True)
    intro_quote2 = models.CharField(default="every hustler's",max_length=200, blank=True,null=True)
    intro_quote3 = models.CharField(default=" life.",max_length=200, blank=True,null=True)
    quoter_name = models.CharField(max_length=200, blank=True,null=True)
    quoter_title = models.CharField(max_length=200, blank=True,null=True)

    body = RichTextField(blank=True)

    designer = models.CharField(max_length=200, blank=True,null=True)
    # latest_news = 

    content_panels=Page.content_panels + [
        FieldPanel('body',classname = "full"),
        FieldPanel('faicon'),
        FieldPanel('image0'),
        FieldPanel('signature_01'),
        FieldPanel('logo'),
        FieldPanel('logo1'),
        FieldPanel('logofooter'),

        FieldPanel('intro_quote1'),
        FieldPanel('intro_quote2'),
        FieldPanel('intro_quote3'),

        FieldPanel('quoter_name'),
        FieldPanel('quoter_title'),
        FieldPanel('designer'),
        InlinePanel('latestnewz',label="Latest News")

    ]


class LatestNews(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='latestnewz')
    title = models.CharField(max_length=250)
    date = models.DateField("Post Date")
    url = models.CharField(max_length=250 ,blank=True,null=True)
    link =  models.URLField(blank=True)

    panels = [
        FieldPanel('title'),
        FieldPanel('date'),
        # FieldPanel('caption'),
    ]