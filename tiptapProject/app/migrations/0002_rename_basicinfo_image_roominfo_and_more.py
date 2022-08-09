# Generated by Django 4.0 on 2022-08-07 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='basicInfo',
            new_name='roomInfo',
        ),
        migrations.AlterField(
            model_name='room',
            name='brokerAgency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.brokeragency'),
        ),
    ]
