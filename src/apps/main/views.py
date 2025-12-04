from django.views import generic

from . import models


class HomeView(generic.TemplateView):
    template_name = 'main/home/index.django-html'


class AboutUsView(generic.TemplateView):
    template_name = 'main/about-us.django-html'


class ContactUsView(generic.TemplateView):
    template_name = 'main/contact-us.django-html'


class ExcursionListView(generic.ListView):
    model = models.Excursion
    template_name = 'main/excursion-list.django-html'
    ordering = ('created_at')


class ExcursionDetailView(generic.DetailView):
    model = models.Excursion
    template_name = 'main/excursion-detail/index.django-html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return models.Excursion.objects.filter(is_published=True)
