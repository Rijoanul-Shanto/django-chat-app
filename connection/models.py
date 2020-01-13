from django.contrib.auth.models import User
from django.db import models


class ConnectionRequest(models.Model):
    who = models.ForeignKey(User, on_delete=models.CASCADE)
    whom = models.ForeignKey(User, on_delete=models.CASCADE)


class Connection(models.Model):
    who = models.ForeignKey(User, on_delete=models.CASCADE)
    whom = models.ForeignKey(User, on_delete=models.CASCADE)


class ConnectionBlock(models.Model):
    who = models.ForeignKey(User, on_delete=models.CASCADE)
    whom = models.ForeignKey(User, on_delete=models.CASCADE)
