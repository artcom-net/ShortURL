import random
import string

from django.conf import settings
from django.db import models
from django.core.validators import URLValidator
# Create your models here.
from django.urls import reverse


SHORT_CODE_LENGTH = getattr(settings, 'SHORT_CODE_LENGTH', 6)
HOSTNAME = getattr(settings, 'HOSTNAME', 'localhost')
PORT = getattr(settings, 'PORT', '8000')
PROTOCOL = getattr(settings, 'PROTOCOL', 'http')


class ShortURLManager(models.Manager):

    @staticmethod
    def get_active_url():
        return ShortURL.objects.filter(is_active=True)


class ShortURL(models.Model):

    url = models.CharField(max_length=200, validators=(URLValidator(),))
    short_code = models.CharField(max_length=20, unique=True, null=True,
                                  blank=True)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    objects = ShortURLManager()

    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = self.gen_short_code()
        super(ShortURL, self).save(*args, **kwargs)

    def gen_short_code(self):
        chars = string.ascii_uppercase + string.digits
        code = ''.join(random.choice(chars) for _ in range(SHORT_CODE_LENGTH))
        class_ = self.__class__
        if class_.objects.filter(short_code=code).exists():
            return self.gen_short_code()
        return code

    def get_short_url(self):
        path = reverse('short_url', kwargs={'short_code': self.short_code})
        return '{protocol}://{hostname}:{port}{path}'.format(
            protocol=PROTOCOL, hostname=HOSTNAME, port=PORT, path=path
        )

    def __str__(self):
        return str(self.url)
