from django.db import models


class User(models.Model):
    registered = models.DateTimeField(auto_now_add=True)
    loyalty_status = models.CharField(max_length=100, null=True)

