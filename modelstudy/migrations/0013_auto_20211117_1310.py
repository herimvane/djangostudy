# Generated by Django 3.2.9 on 2021-11-17 05:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modelstudy', '0012_auto_20211117_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='parent_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='modelstudy.comment'),
        ),
        migrations.AlterField(
            model_name='person',
            name='friends',
            field=models.ManyToManyField(blank=True, null=True, related_name='_modelstudy_person_friends_+', to='modelstudy.Person'),
        ),
    ]