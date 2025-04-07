from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page, name='home_page'),
    path('business',views.business_page, name='business_page'),
    path('projects',views.projects_page, name='projects_page'),
    path('products',views.products_page, name='products_page'),
    path('training',views.training_page, name='training_page'),
    path('contactus',views.contact_page, name='contact_page'),
    path('sendmail', views.send_mail_page,name='sendmail'),
    

]