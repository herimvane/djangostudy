import uuid

from django.conf import settings
from django.db import models


# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=30, verbose_name='name of school')

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=30, verbose_name='name of student')
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students', related_query_name='stu',
                               verbose_name='school of student')

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=30)
    roles = models.ManyToManyField('Role')

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Comment(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Person(models.Model):
    name = models.CharField(max_length=30)
    friends = models.ManyToManyField("self", null=True, blank=True)

    def __str__(self):
        return self.name
