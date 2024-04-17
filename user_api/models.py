from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length = 50, null=False)
    middle_name = models.CharField(max_length = 50, null=True, blank=True)
    last_name = models.CharField(max_length = 50, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user_id)
