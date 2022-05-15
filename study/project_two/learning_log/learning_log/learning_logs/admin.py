from django.contrib import admin

from learning_logs.models import Topic, Entry


# Import the registered model and manage it through the 'Django' website
admin.site.register(Topic)
admin.site.register(Entry)
