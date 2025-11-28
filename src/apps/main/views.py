from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'main/home/index.django-html'


class AboutUsView(TemplateView):
    template_name = 'main/about-us.django-html'


class ContactUsView(TemplateView):
    template_name = 'main/contact-us.django-html'


class ExcursionListView(generic.ListView):
    model = models.Excursion
    template_name = 'main/excursion-list.django-html'
    ordering = ("created_at",)


class ExcursionDetailView(TemplateView):
    template_name = 'main/excursion-detail.django-html'
