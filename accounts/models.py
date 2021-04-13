from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from student.models import Student


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'parent'),
        (2, 'teacher'),
        (3, 'secretary'),
        (4, 'headteacher'),
        (5, 'admin'),
    )

    user_type = models.PositiveSmallIntegerField(
        choices=USER_TYPE_CHOICES, null=True, blank=True)


class Profile(models.Model):
    GENDER_CHOICES = (
        (1, 'Male'), (2, 'Female')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_no = models.IntegerField(max_length=50, blank=True)
    phone_number = models.IntegerField(max_length=30, blank=True)
    profession = models.CharField(null=True, blank=True)
    gender = models.PositiveSmallIntegerField(
        GENDER_CHOICES, null=True, blank=True)
    student = models.ManyToManyField(Student)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
