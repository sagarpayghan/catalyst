from django.db import models

# Create your models here.
class CompanyModel(models.Model):
    id=models.IntegerField(primary_key=True,null=False)
    name=models.CharField(max_length=100)
    domain=models.CharField(max_length=100)
    year_founded=models.DateField()
    industry=models.CharField(max_length=100)
    size_range=models.CharField(max_length=100)
    locality=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    linkedin_url=models.CharField(max_length=100)
    current_employee_estimate=models.IntegerField()
    total_employee_estimate=models.IntegerField()

    def __str__(self):
        return self.name