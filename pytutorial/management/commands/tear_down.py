__author__ = 'robert'
from django.core.management import BaseCommand
from django.core.management import call_command
from stream_twitter.models import *
from stream_django.feed_manager import feed_manager


class Command(BaseCommand):
    def handle(self, *args, **options):
        feed_manager.enable_model_tracking()

        Tweet.objects.all().delete()
        Follow.objects.all().delete()
        UserProfile.objects.all().delete()
        User.objects.all().delete()
        Hashtag.objects.all().delete()

        self.print_users()

    def print_users(self):
        for user in User.objects.all():
            print(user)
