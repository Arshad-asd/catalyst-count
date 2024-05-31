from django.db import models

class Upload(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class CompanyData(models.Model):
    keyword = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    year_founded = models.IntegerField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    employees_from = models.IntegerField()
    employees_to = models.IntegerField()

    def __str__(self):
        return f"{self.keyword} - {self.industry} - {self.city}, {self.state}, {self.country}"
