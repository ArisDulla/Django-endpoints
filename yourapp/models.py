from django.db import models


#
# Create your models here.
#
class Turbines(models.Model):
    name = models.CharField(max_length=100)
    lat = models.FloatField()
    long = models.FloatField()
    power = models.IntegerField()


# ---------------------------------------------------
#
# Employers + ROLES
#
class Employers(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.id.__str__()


class Departments(models.Model):
    name = models.CharField(max_length=100)
    roof = models.IntegerField()
    office = models.IntegerField()

    employers = models.ManyToManyField(
        Employers,
        through='Roles',
        through_fields=('departments', 'employers'),
    )

    def __str__(self):
        return self.name


class Roles(models.Model):
    departments = models.ForeignKey(Departments, on_delete=models.CASCADE)
    employers = models.ForeignKey(Employers, on_delete=models.CASCADE)
    date = models.DateField()
    details = models.CharField(max_length=100)
