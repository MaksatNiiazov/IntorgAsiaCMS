from django.core.exceptions import ValidationError


class SingletonModelMixin:
    def clean(self):
        if self.__class__.objects.exists() and not self.pk:
            raise ValidationError(f'There can be only one {self.__class__.__name__} instance.')

    def save(self, *args, **kwargs):
        if not self.pk and self.__class__.objects.exists():
            raise ValidationError(f'There can be only one {self.__class__.__name__} instance.')
        return super().save(*args, **kwargs)
