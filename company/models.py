from django.db import models

# Create your models here.
from django.db import models


class Branch(models.Model):
    name = models.CharField(null=False, blank=False, max_length=150)
    address = models.CharField(null=False, blank=False,max_length=255)
    pincode = models.BigIntegerField()

    def __unicode__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(null=False, blank=False, max_length=150)
    reg_no = models.CharField(null=False, blank=False, max_length=255)
    banch = models.ForeignKey(Branch, null=False, blank=False, on_delete=models.PROTECT)

    def __unicode__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(null=False, blank=False, max_length=150)
    last_name = models.CharField(null=False, blank=False, max_length=150)
    appointed_banch = models.ForeignKey(Branch, on_delete=models.PROTECT)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    dob = models.DateField(null=False, blank=False)
    address = models.CharField(null=False, blank=False, max_length=150)
    shift_intime = models.DateTimeField(null=False, blank=False)
    shift_outtime = models.DateTimeField(null=False, blank=False)
    pan_number = models.CharField(null=True, blank=True, max_length=20)
    aadhar_number = models.CharField(null=True, blank=True, max_length=20)

    class meta():
        abstract = True
        unique_together = ('company', 'pan_number', 'aadhar_number')

    def __unicode__(self):
        return '{0}.{1}'.format(self.first_name, self.dob)


class Employer(models.Model):
    first_name = models.CharField(null=False, blank=False, max_length=150)
    last_name = models.CharField(null=False, blank=False, max_length=150)
    dob = models.DateField(null=False, blank=False)
    address = models.CharField(null=False, blank=False, max_length=150)
    banch = models.ForeignKey(Branch, on_delete=models.PROTECT)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    pan_number = models.CharField(null=True, blank=True, max_length=20)
    aadhar_number = models.CharField(null=True, blank=True, max_length=20)

    class meta():
        abstract = True
        unique_together = ('company', 'pan_number', 'aadhar_number')

    def __unicode__(self):
        return '{0}.{1}'.format(self.first_name, self.dob)


class Designation(models.Model):
    d_name = models.CharField(null=False, blank=False, max_length=150)
    grade = models.CharField(null=True, blank=True, max_length=15)
    position = models.CharField(null=True, blank=True, max_length=100)

    def __unicode__(self):
        return self.d_name