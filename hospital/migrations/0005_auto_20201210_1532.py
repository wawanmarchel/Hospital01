# Generated by Django 3.1.1 on 2020-12-10 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0004_auto_20201210_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='nurse',
            field=models.ManyToManyField(null=True, to='hospital.Nurse'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='room',
            field=models.ManyToManyField(null=True, to='hospital.Room'),
        ),
    ]
