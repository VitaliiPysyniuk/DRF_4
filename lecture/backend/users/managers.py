from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_standard_user(self, password, email, **extra_kwargs):
        if not email:
            raise Exception('No email')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_super_user(self, password, email, **extra_kwargs):
        extra_kwargs.setdefault('is_staff', True)
        extra_kwargs.setdefault('is_superuser', True)
        extra_kwargs.setdefault('is_active', True)

        if not extra_kwargs.get('is_staff'):
            raise Exception('Must be is_staff True')
        if not extra_kwargs.get('is_superuser'):
            raise Exception('Must be is_superuser True')
        return self.create_standard_user(email=email, password=password, **extra_kwargs)
