# Generated by Django 3.2.9 on 2021-11-16 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modelstudy', '0005_auto_20211116_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='modelstudy.school', verbose_name='school of student'),
        ),
    ]