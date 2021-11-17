# Generated by Django 3.2.9 on 2021-11-17 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelstudy', '0007_alter_student_school'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('roles', models.ManyToManyField(to='modelstudy.Role')),
            ],
        ),
    ]