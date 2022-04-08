from django.db import models
from django.utils.translation import gettext as _
# Create your models here.

class Scraper(models.Model):
    url = models.CharField(_("URL"),null=False,blank=False,help_text="Enter URL",max_length=10000)
    img_link = models.TextField(_("Image Link"))
    href_link = models.TextField(_("Web page Link"))

    def __str__(self) :
        return self.url
    
    class Meta:
        ordering = ('-id',)