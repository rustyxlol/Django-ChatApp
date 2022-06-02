# File that runs when a user is created, a trigger to create Profiles
# straightforward - sender, reciever

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        # Create profile whenever a user is created
        Profile.objects.create(user=instance)
        # Tie it to the receiver decorator


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

# Add the following to admin.py
# def ready(self):
#     import users.signals
