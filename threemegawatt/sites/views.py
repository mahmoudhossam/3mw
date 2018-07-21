from django.views.generic import TemplateView
from django.db.models import Avg
from .models import Site, Values


class SiteListView(TemplateView):
    template_name = "pages/sites.html"

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        kwargs['sites'] = Site.objects.all()
        return kwargs


class SiteDetailView(TemplateView):
    template_name = "detail.html"

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        try:
            site = Site.objects.get(id=kwargs['id'])
            kwargs['site'] = site
            kwargs['values'] = Values.objects.filter(site=site)
        except Site.DoesNotExist:
            pass
        return kwargs


class SummaryView(TemplateView):
    template_name = "pages/summary.html"

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        values = {}
        for val in Values.objects.all():
            site_name = val.site.name
            if site_name in values:
                values[site_name]['a_value'] += val.a_value
                values[site_name]['b_value'] += val.b_value
            else:
                values[site_name] = {'a_value': val.a_value,
                                     'b_value': val.b_value}
        kwargs['values'] = values
        return kwargs


class AverageView(TemplateView):
    template_name = "pages/summary-average.html"

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)
        query = ("SELECT v.id, s.name, AVG(v.a_value) AS a_value, AVG(v.b_value) AS b_value "
                 "FROM sites_values v LEFT OUTER JOIN sites_site s "
                 "ON v.site_id = s.id GROUP BY s.id;")
        values = Values.objects.raw(query)
        kwargs['values'] = values
        return kwargs
