# Generated by Django 3.0 on 2021-06-22 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0006_auto_20210622_1451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modelfields',
            name='binNum',
        ),
        migrations.AlterField(
            model_name='modelfields',
            name='HaveLaptop',
            field=models.BooleanField(default=False),
        ),
    ]