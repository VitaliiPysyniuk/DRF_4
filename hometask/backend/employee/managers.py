from django.db.models import Manager


class EmployeeManager(Manager):
    def create(self, **extra_kwargs):
        company = extra_kwargs.pop('company')
        is_employed = extra_kwargs.pop('is_employed')
        if company and not is_employed:
            raise Exception('Employee must be employed')
        if not company and is_employed:
            raise Exception('Employee must have work company')
        is_employed = extra_kwargs.pop('is_employed')

        employee = self.model(is_employed=is_employed, **extra_kwargs)
        employee.save()
        return employee
