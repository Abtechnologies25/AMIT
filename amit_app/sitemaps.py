from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return ['home_page', 'business_page', 'projects_page','training_page','contact_page','gallery_view']  # Update with your actual view names

    def location(self, item):
        return reverse(item)
