# Generated by Django 3.2.9 on 2021-11-17 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelstudy', '0008_role_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friends', models.ManyToManyField(related_name='_modelstudy_person_friends_+', to='modelstudy.Person')),
            ],
        ),
    ]
