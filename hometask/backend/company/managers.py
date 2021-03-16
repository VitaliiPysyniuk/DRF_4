from django.db.models import Manager


class CompanyManager(Manager):
    def create(self, **extra_kwargs):
        company = self.model(**extra_kwargs)
        company.save()
        return company

