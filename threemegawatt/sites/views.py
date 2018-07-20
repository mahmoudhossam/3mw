from django.views.generic import TemplateView
from .models import Site, Values


class SitesView(TemplateView):
    template_name = "pages/sites.html"

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        kwargs['sites'] = Site.objects.all()
        return kwargs


class SummaryView(TemplateView):
    template_name = "pages/summary.html"

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        kwargs['values'] = Values.objects.all()
        return kwargs
