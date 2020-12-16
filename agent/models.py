from django.db import models


class Company(models.Model):
    name_company = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=18)
    category = models.CharField(max_length=60)

    def __str__(self):
        return self.name_company


class SalesRepresentative(models.Model):
    name_agent = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=16)
    agent_company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_agent
