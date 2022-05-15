from django.db import models


class Topic(models.Model):
    """User learning topics"""

    text = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns the string representation of the model"""
        return self.text


class Entry(models.Model):
    """Something specific about a subject that you have learned"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    data_added = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return the string representation of the model"""
        return self.text[:50] + "..."
