from django.db import models
from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel ,InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel 
from wagtail.search import index
from django.utils.translation import gettext_lazy as _
from django.conf import settings


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
    latest_new_title = models.CharField(max_length=200, default='Latest News', blank=True,null=True)

    call_no =  models.CharField(max_length=200, default='020 2020 405', blank=True,null=True)

    info_mail = models.EmailField(default='info@uda-party.com')
    office_location = models.CharField(max_length=200,default="Hustler Center | Nairobi Kenya", blank=True,null=True)

    designer = models.CharField(max_length=200, default='+254712748566', blank=True,null=True)
    designer_link = models.URLField(default="https://www.linkedin.com/in/kipngeno-gibeon-27b9765a/")
    
    join_tittlea = models.CharField(max_length=250 ,blank=True,null=True)
    join_tittleb = models.CharField(max_length=250 ,blank=True,null=True)
    join_tittlec = models.CharField(max_length=250 ,blank=True,null=True)


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
        FieldPanel('latest_new_title'),


        FieldPanel('office_location'),
        FieldPanel('info_mail'),
        FieldPanel('call_no'),
        FieldPanel('designer_link'),

        InlinePanel('latestnewz',label="Latest News"),
        InlinePanel('latestinfo',label="Latest Info"),
        InlinePanel('twitz',label="Twiter Massages"),


        FieldPanel('join_tittlea'),
        FieldPanel('join_tittleb'),
        FieldPanel('join_tittlec'),

    ]






class LatestNews(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='latestnewz')
    title = models.CharField(max_length=250, blank=True)
    image_n = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE,related_name='+',blank=True ,null =True)
    image = models.ImageField(upload_to='images/newsimage/%Y/%m/%d/',max_length=2000,blank=True ,null =True)
    date = models.DateField("Post Date")
    url = models.CharField(max_length=250 ,blank=True,null=True)
    link =  models.URLField(blank=True)


    panels = [
        FieldPanel('title'),
        # FieldPanel('image'),
        FieldPanel('image_n'),
        FieldPanel('date'),
        FieldPanel('url'),
        FieldPanel('link'),
    ]

    # def get_context(self, request):
    #     context = super().get_context(request)
    #     latestnewz = self.get_children().live()[-3]
    #     context['latestnewz'] = latestnewz
    #     return context


class LatestInfo(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='latestinfo')
    title = models.CharField(max_length=250, blank=True)
    image = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE,related_name='+',blank=True ,null =True)
    # image = models.ImageField(upload_to='images/newsimage/%Y/%m/%d/',max_length=2000,blank=True ,null =True)
    date = models.DateField("Post Date")
    url = models.CharField(max_length=250 ,blank=True,null=True)
    link =  models.URLField(blank=True)

    panels = [
        FieldPanel('title'),
        # FieldPanel('image'),
        FieldPanel('image'),
        FieldPanel('date'),
        FieldPanel('url'),
        FieldPanel('link'),
    ]


class Twit(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='twitz')
    title = models.CharField(max_length=250, blank=True)
    image = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE,related_name='+',blank=True ,null =True)
    twit = models.CharField(max_length=250 ,blank=True,null=True)
    
    date = models.DateField("Post Date")
    url = models.CharField(max_length=250 ,blank=True,null=True)
    link =  models.URLField(blank=True)
    linkname = models.CharField(max_length=250 ,blank=True,null=True)




    panels = [
        FieldPanel('title'),
        FieldPanel('linkname'),
        FieldPanel('image'),
        FieldPanel('twit'),
        FieldPanel('date'),
        FieldPanel('url'),
        FieldPanel('link'),


    ]



class Donate(Page):
    image0 = models.ImageField(upload_to='images/donate/%Y/%m/%d/',max_length=2000,blank=True ,null =True)

    header1 = models.CharField(default="Help us reach our goals",max_length=200, blank=True,null=True)
    header2 = models.CharField(default="Donate for",max_length=200, blank=True,null=True)
    header3 = models.CharField(default="Victory",max_length=200, blank=True,null=True)

    title0 = models.CharField(default="Thank you for supporting our work!",max_length=200, blank=True,null=True)
    title1a = models.CharField(default="",max_length=200, blank=True,null=True)
    title1b = models.CharField(default="",max_length=200, blank=True,null=True)

    body = RichTextField(blank=True)

    logo = models.ImageField(upload_to='images/logo/%Y/%m/%d/',max_length=2000,blank=True ,null =True)
    logo1 = models.ImageField(upload_to='images/logo/%Y/%m/%d/',max_length=2000,blank=True ,null =True)

    logofooter = models.ImageField(upload_to='images/logo/%Y/%m/%d/',max_length=2000,blank=True ,null =True)


    mlink =  models.URLField(blank=True)


    content_panels=Page.content_panels + [
        FieldPanel('body',classname = "full"),
        FieldPanel('image0'),

        FieldPanel('header1'),
        FieldPanel('header2'),
        FieldPanel('header3'),

        FieldPanel('title0'),
        FieldPanel('title1a'),
        FieldPanel('title1b'),



        FieldPanel('logo'),
        FieldPanel('logo1'),
        FieldPanel('logofooter'),

        FieldPanel('mlink'),


        # InlinePanel('latestnewz',label="Latest News"),

    ]

class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    # is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Checkout(TimeStamp):
    # user = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.CASCADE,
    #     related_name="checkouts",
    #     blank=True,
    #     null=True,
    # )
    # email = models.EmailField(blank=True, null=True)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    paid = models.BooleanField(default=False, blank=True, null=True)
    # success = models.BooleanField(default=False, blank=True, null=True)

    def save(self, *args, **kwargs):
        if abs(self.amount) == 0:
            self.amount = 1
        else:
            self.amount = abs(self.amount)
        super().save(*args, **kwargs)