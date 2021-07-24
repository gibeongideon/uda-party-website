from django.db import models
from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel ,InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel 
from wagtail.search import index
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from django.utils.translation import gettext_lazy as _
from django.conf import settings


class HomePage(Page):
    
    image0 = models.ImageField(upload_to='images/intro/%Y/%m/%d/',max_length=2000,blank=True ,null =True)
    signature_01 = models.ImageField(upload_to='images/signature/%Y/%m/%d/',max_length=2000,blank=True ,null =True)
    intro_quote1 = models.CharField(default="Our quest to empower & change ",max_length=200, blank=True,null=True)
    intro_quote2 = models.CharField(default="every hustler's",max_length=200, blank=True,null=True)
    intro_quote3 = models.CharField(default=" life.",max_length=200, blank=True,null=True)
    quoter_name = models.CharField(max_length=200, blank=True,null=True)
    quoter_title = models.CharField(max_length=200, blank=True,null=True)

    body = RichTextField(blank=True)
    latest_new_title = models.CharField(max_length=200, default='Latest News', blank=True,null=True)
    
    join_tittlea = models.CharField(max_length=250 ,blank=True,null=True)
    join_tittleb = models.CharField(max_length=250 ,blank=True,null=True)
    join_tittlec = models.CharField(max_length=250 ,blank=True,null=True)

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
        FieldPanel('signature_01'),


        FieldPanel('intro_quote1'),
        FieldPanel('intro_quote2'),
        FieldPanel('intro_quote3'),

        FieldPanel('quoter_name'),
        FieldPanel('quoter_title'),
        FieldPanel('latest_new_title'),

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


    mlink =  models.URLField(blank=True)
    plink =  models.URLField(blank=True)

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

        FieldPanel('header1'),
        FieldPanel('header2'),
        FieldPanel('header3'),

        FieldPanel('title0'),
        FieldPanel('title1a'),
        FieldPanel('title1b'),

        FieldPanel('mlink'),
        FieldPanel('plink'),


        # InlinePanel('latestnewz',label="Latest News"),

    ]



@register_snippet
class Advert(models.Model):
    url = models.URLField(null=True, blank=True)
    text = models.CharField(max_length=255)

    panels = [
        FieldPanel('url'),
        FieldPanel('text'),
    ]

    def __str__(self):
        return self.text


@register_snippet
class Header(models.Model):
    faicon = models.ImageField(upload_to='images/faricon/%Y/%m/%d/',max_length=2000,blank=True ,null =True)
    url = models.URLField(null=True, blank=True)
    text = models.CharField(max_length=255,blank=True,null=True)
    logo = models.ImageField(upload_to='images/logo/%Y/%m/%d/',max_length=2000,blank=True ,null =True)
    logo1 = models.ImageField(upload_to='images/logo/%Y/%m/%d/',max_length=2000,blank=True ,null =True)

    

    panels = [
        FieldPanel('url'),
        FieldPanel('text'),
        FieldPanel('logo'),
        FieldPanel('logo1'),
        FieldPanel('faicon'),

        
    ]

    def __str__(self):
        return self.text


@register_snippet
class Footer(models.Model):
    url = models.URLField(null=True, blank=True)
    text = models.CharField(max_length=255, blank=True,null=True)
    logofooter = models.ImageField(upload_to='images/logo/%Y/%m/%d/',max_length=2000,blank=True ,null =True)

    call_no =  models.CharField(max_length=200, default='020 2020 405', blank=True,null=True)
    info_mail = models.EmailField(default='info@uda-party.com')
    office_location = models.CharField(max_length=200,default="Hustler Center | Nairobi Kenya", blank=True,null=True)
    designer = models.CharField(max_length=200, default='+254712748566', blank=True,null=True)
    designer_link = models.URLField(default="https://www.linkedin.com/in/kipngeno-gibeon-27b9765a/")

    panels = [
        FieldPanel('url'),
        FieldPanel('text'),
        
        FieldPanel('logofooter'),

        FieldPanel('office_location'),
        FieldPanel('info_mail'),
        FieldPanel('call_no'),
        FieldPanel('designer'),
        FieldPanel('designer_link'),
    ]

    def __str__(self):
        return self.text