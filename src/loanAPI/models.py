from django.db import models

# Create your models here.
class Approvals(models.Model):
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female")
    )
    MARRIED_CHOICES = (
        ("Yes", "Yes"),
        ("No", "No")
    )
    GRADUATED_CHOICES = (
        ("Graduate", "Graduate"),
        ("Not_Graduate", "Not_Graduate")
    )
    SELFEMPLOYED_CHOICES = (
        ("Yes", "Yes"),
        ("No", "No")
    )
    PROPERY_CHOICES = (
        ("Rural", "Rural"),
        ("Semiurban", "Semiurban"),
        ("Urban", "Urban")
    )

    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    dependants = models.IntegerField()
    applicant_income = models.IntegerField()
    coapplicant_income = models.IntegerField()
    loan_amt = models.IntegerField()
    loan_term = models.IntegerField()
    credit_history = models.IntegerField()
    gender = models.CharField(max_length=15)
    married = models.CharField(max_length=15)
    graduated_education = models.CharField(max_length=15)
    self_employed = models.CharField(max_length=15)
    area = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.firstname, self.lastname
