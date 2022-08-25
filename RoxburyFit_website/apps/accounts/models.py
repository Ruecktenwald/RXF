from django.db import models

class UserProfile(models.Model):

    is_full_name_displayed = models.BooleanField(default=True)

#edit to test git
