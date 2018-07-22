from django.db.models import Manager


class ValuesManager(Manager):

    def average(self):
        query = ("SELECT v.id, s.name, AVG(v.a_value) AS a_value, AVG(v.b_value) AS b_value "
                 "FROM sites_values v LEFT OUTER JOIN sites_site s "
                 "ON v.site_id = s.id GROUP BY s.id;")
        return self.raw(query)

    def sum(self):
        values = {}
        for val in self.all():
            site_name = val.site.name
            if site_name in values:
                values[site_name]['a_value'] += val.a_value
                values[site_name]['b_value'] += val.b_value
            else:
                values[site_name] = {'a_value': val.a_value,
                                     'b_value': val.b_value}
        return values
