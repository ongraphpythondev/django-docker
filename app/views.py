from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .scrape import img_scrape,href_scrape
from .models import Scraper

class ScraperCreateView(View):
    template_name = "home.html"
    def get(self, request) :
        return render(request, "home.html", {"scrapes" : Scraper.objects.all()})
    
    def post(self, request):
        url = str(request.POST.get("URL"))
        href = href_scrape(url)
        img = img_scrape(url)
        if url :
            scrape = Scraper.objects.create(url=url,img_link=img,href_link=href)
            scrape.save()
        return render(request, "home.html", {"scrape" : Scraper.objects.all()})

        
