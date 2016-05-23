from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class QuerySet(models.QuerySet):
    def get_speaker(self):
        return "%s %s"%(self.Degree, self.Name)


class Members(models.Model):
    id = models.AutoField(primary_key = True)
    User = models.OneToOneField(User)
    Name = models.CharField(max_length = 15)
    Last_Name = models.CharField(max_length = 15)
    STATUS = (
        ('AD', 'Administrator'),
        ('AC', 'Assistance Coordinator'),
        ('PC', 'Presentations Coordinator'),
        ('SC', 'Staff Coordinator'),
    )
    Position = models.CharField(max_length = 2, choices = STATUS, default = 'Position')

    class Meta:
        permissions = (('is_admin','Administrator'),('is_ac', 'AssistanceCoordinator'),('is_pc', 'PresentationsCoordinator'),('is_sc', 'StaffCoordinator'))

    def __unicode__(self):
        return 'Name: %s - Position: %s' %(self.Name, self.Position)


class Speaker(models.Model):
    id = models.AutoField(primary_key = True)
    DEGREES = (
        ('Doc', 'Doctor'),
        ('Lic', 'Licenciado'),
        ('Ing', 'Ingeniero'),
        ('MC', 'Maestro en Ciencias')
    )
    Degree = models.CharField(max_length = 3, choices = DEGREES, default = 'Degree')
    Name = models.CharField(max_length = 15)
    Last_Name = models.CharField(max_length = 15)
    Picture = models.ImageField(upload_to='img_speakers/', null = True)
    objects = QuerySet.as_manager()

    def __unicode__(self):
        return 'Name: %s %s' %(self.Degree, self.Name)

class Conference(models.Model):
    id = models.AutoField(primary_key = True)
    Title = models.CharField(max_length = 30)
    Description = models.CharField(max_length = 150)
    Speaker = models.OneToOneField(Speaker)
    Date = models.DateField(auto_now = False)
    Time = models.TimeField(auto_now = False)
    Image = models.ImageField(upload_to = 'img_conference/', null = True)

    def __unicode__(self):
        return self.Title

class Assistant(models.Model):
    id = models.AutoField(primary_key = True)
    Name = models.CharField(max_length = 15)
    Last_Name = models.CharField(max_length = 15)
    Age = models.IntegerField()
    email = models.EmailField(max_length = 30)

    def __unicode__(self):
        return 'Name: %s - E-mail: %s' %(self.Name, self.email)

class Staff(models.Model):
    id = models.AutoField(primary_key = True)
    Name = models.CharField(max_length = 15)
    Task = models.CharField(max_length = 50)
    Phone = models.IntegerField()

    def __unicode__(self):
        return self.Name
