# Generated by Django 3.1.1 on 2020-12-10 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0005_auto_20201210_1532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='nurse',
        ),
        migrations.AddField(
            model_name='doctor',
            name='nurse',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital.nurse'),
        ),
        migrations.RemoveField(
            model_name='patient',
            name='room',
        ),
        migrations.AddField(
            model_name='patient',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital.room'),
        ),
    ]