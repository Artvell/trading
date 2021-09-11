from django.db import models
from django.contrib.auth import get_user_model

class Verification(models.Model):
    objects = models.Manager()
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE,related_name="verif_code")
    verification_code = models.IntegerField(editable=False)

    def __str__(self):
        return str(self.verification_code)