from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel

__all__ = ('Customer',)


class Customer(TimeStampedModel):
    name = models.CharField('客戶名稱', max_length=200, blank=True, null=True)
    tax_id = models.CharField('統一編號' ,max_length=20, blank=True, null=True)
    phone = models.CharField('聯絡電話', max_length=20, blank=True, null=True)
    address = models.CharField('送貨地址', max_length=20, null=True, blank=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']