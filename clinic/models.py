from django.db import models

# Create your models here.

class Disease(models.Model):
    name = models.CharField(max_length=100)
    description= models.TextField(blank=True, null=True)
    sample_image = models.ImageField(upload_to='disease_images/', blank=True, null=True)

    deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.description}"

class Symptom(models.Model):
    disease= models.ForeignKey(Disease, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    description= models.CharField(max_length=200, blank=True, null=True)

    deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.disease} -> {self.name} - {self.description}"
    
class Reason(models.Model):
    disease= models.ForeignKey(Disease, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    description= models.TextField(blank=True, null=True)

    deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.disease} -> {self.name} - {self.description}"
    
class Treatment(models.Model):
    disease= models.ForeignKey(Disease, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    description= models.TextField(blank=True, null=True)

    deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.disease} -> {self.name} - {self.description}"

    
class Speciality(models.Model):
    disease= models.OneToOneField(Disease, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=100)
    details= models.TextField()
    sample_image = models.ImageField(upload_to='speciality_images/', blank=True)

    deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.name}"
