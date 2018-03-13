from django.conf.urls import url, include
from . import views

# This is app_one
urlpatterns = [
# root route to main method
    url(r'^$', views.index, name='index'),
    # url(r'^main$', views.index, name='main'),
    url(r'^login$', views.login, name='login'),
    url(r'^register$', views.register, name='register'),
    url(r'^logout$', views.logout, name='logout'),

]
