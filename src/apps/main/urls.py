from django.urls import path

from . import views


app_name = 'main'


urlpatterns = (
    path('', views.HomeView.as_view(), name='home'),
    path('about-us/', views.AboutUsView.as_view(), name='about-us'),
    path('contact-us/', views.ContactUsView.as_view(), name='contact-us'),
    path('excursions/', views.ExcursionListView.as_view(), name='excursion-list'),  # noqa
    path('excursions/detail/', views.ExcursionDetailView.as_view(), name='excursion-detail'),  # noqa
)
