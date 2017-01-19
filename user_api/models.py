from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(models.Model):

    user = models.OneToOneField(User)
    current_integer = models.PositiveIntegerField(blank=False, default=0)

    def __unicode__(self):
        return (self.user.email + ' ' + str(self.current_integer))


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        CustomUser.objects.create(user=instance)