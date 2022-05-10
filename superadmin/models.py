from django.db import models
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField

User = get_user_model()

# Create your models here.


class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100,blank=True,null=True)
    last_name = models.CharField(max_length=100)

    phone_no = PhoneNumberField(blank=False, null=False, unique=True)
    address = models.CharField(max_length=100)

    profile_image = models.ImageField(
        upload_to='superadmin_profile_pic/', blank=True)
    
    deleted=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.email} -> {self.first_name}"
