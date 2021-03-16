from django.contrib.auth.models import BaseUserManager


class OwnerManager(BaseUserManager):
    def create_standard_owner(self, email, password, **extra_kwargs):
        if not email:
            raise Exception('No email')
        email = self.normalize_email(email)
        owner = self.model(email=email, **extra_kwargs)
        owner.set_password(password)
        return owner

    def create_super_owner(self, email, password, **extra_kwargs):
        extra_kwargs.setdefault('is_superuser', True)
        if not extra_kwargs.get('is_superuser'):
            raise Exception('Must be superuser')
        return self.create_standard_owner(email=email, password=password, **extra_kwargs)

    def update_owner(self, instance, **extra_kwargs):
        pass


