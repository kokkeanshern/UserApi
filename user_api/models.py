from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, null=False)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=50, null=False)

    def __str__(self):
        return str(self.user_id)
    
class UserPin(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    pin = models.SmallIntegerField()

    def __str__(self):
        return str(self.user.user_id)
