# Generated by Django 4.0.6 on 2022-08-07 19:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_brokeragency_brokeragency_company_registration_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomInfo',
            fields=[
                ('roominfo_id', models.AutoField(primary_key=True, serialize=False)),
                ('basicInfo_location_x', models.DecimalField(decimal_places=7, max_digits=10)),
                ('basicInfo_location_y', models.DecimalField(decimal_places=7, max_digits=10)),
                ('basicInfo_brokerAgency', models.TextField(blank=True, null=True)),
                ('basicInfo_move_in_date', models.TextField(blank=True, null=True)),
                ('basicInfo_brokerAgency_contact', models.CharField(max_length=20, null=True, validators=[django.core.validators.RegexValidator(regex='^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$')])),
                ('basicInfo_room_type', models.CharField(blank=True, choices=[('J', 'Jeonse'), ('BJ', 'Ban Jeonse'), ('M', 'Monthly Rent'), ('', 'not selected')], max_length=2, null=True)),
                ('basicInfo_deposit', models.IntegerField(blank=True, null=True)),
                ('basicInfo_monthly_rent', models.IntegerField(blank=True, null=True)),
                ('basicInfo_maintenance_fee', models.IntegerField(blank=True, null=True)),
                ('basicInfo_floor', models.IntegerField(blank=True, null=True)),
                ('basicInfo_area', models.FloatField(blank=True, null=True)),
                ('basicInfo_number_of_rooms', models.CharField(blank=True, choices=[('1', '1 Room'), ('1.5', '1.5 Room'), ('2', '2 Room'), ('3', '3 Room'), ('', 'not selected')], max_length=3, null=True)),
                ('basicInfo_interior_structure', models.CharField(blank=True, choices=[('O', 'Open'), ('K', 'Kitchen separate Type'), ('V', 'Veranda separate Type'), ('L', 'Double Decker Type'), ('KV', 'Kitchen Veranda separate Type'), ('', 'not selected')], max_length=2, null=True)),
                ('option_gas_stove', models.BooleanField(default=False)),
                ('option_induction', models.BooleanField(default=False)),
                ('option_microwave', models.BooleanField(default=False)),
                ('option_refrigerator', models.BooleanField(default=False)),
                ('option_washing_machine', models.BooleanField(default=False)),
                ('option_air_conditioner', models.BooleanField(default=False)),
                ('option_internet', models.BooleanField(default=False)),
                ('option_tv', models.BooleanField(default=False)),
                ('option_wifi', models.BooleanField(default=False)),
                ('option_closet', models.BooleanField(default=False)),
                ('option_cabinet', models.BooleanField(default=False)),
                ('option_shoe_rack', models.BooleanField(default=False)),
                ('option_bed', models.BooleanField(default=False)),
                ('option_desk', models.BooleanField(default=False)),
                ('option_chair', models.BooleanField(default=False)),
                ('option_drying_rack', models.BooleanField(default=False)),
                ('detailInfo_is_moldy', models.BooleanField(null=True)),
                ('detailInfo_is_leak', models.BooleanField(null=True)),
                ('detailInfo_is_bug', models.BooleanField(null=True)),
                ('detailInfo_is_crack', models.BooleanField(null=True)),
                ('detailInfo_soundproof', models.CharField(blank=True, choices=[('A', 'good'), ('B', 'fair'), ('C', 'poor'), ('', 'not selected')], max_length=1, null=True)),
                ('detailInfo_window_size', models.CharField(blank=True, choices=[('L', 'large'), ('M', 'medium'), ('S', 'small'), ('', 'not selected')], max_length=1, null=True)),
                ('detailInfo_main_direction', models.CharField(blank=True, choices=[('E', 'east'), ('W', 'west'), ('S', 'south'), ('N', 'north'), ('', 'not selected')], max_length=1, null=True)),
                ('detailInfo_ventilator', models.CharField(blank=True, choices=[('F', 'fast'), ('N', 'normal'), ('S', 'slow'), ('', 'not selected')], max_length=1, null=True)),
                ('detailInfo_ventilation', models.CharField(blank=True, choices=[('A', 'good'), ('B', 'fair'), ('C', 'poor'), ('', 'not selected')], max_length=1, null=True)),
                ('detailInfo_external_noise', models.CharField(blank=True, choices=[('L', 'large'), ('M', 'medium'), ('S', 'small'), ('', 'not selected')], max_length=1, null=True)),
                ('detailInfo_water_pressure', models.CharField(blank=True, choices=[('S', 'strong'), ('N', 'normal'), ('W', 'weak'), ('', 'not selected')], max_length=1, null=True)),
                ('detailInfo_drainage', models.CharField(blank=True, choices=[('S', 'strong'), ('N', 'normal'), ('W', 'weak'), ('', 'not selected')], max_length=1, null=True)),
                ('detailInfo_hot_water', models.CharField(blank=True, choices=[('S', 'strong'), ('N', 'normal'), ('W', 'weak'), ('', 'not selected')], max_length=1, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='confirmedroom',
            name='checklist',
        ),
        migrations.RemoveField(
            model_name='confirmedroom',
            name='room',
        ),
        migrations.RemoveField(
            model_name='confirmedroom',
            name='user',
        ),
        migrations.RemoveField(
            model_name='brokersmanner',
            name='user',
        ),
        migrations.RemoveField(
            model_name='checklist',
            name='basicInfo',
        ),
        migrations.RemoveField(
            model_name='checklist',
            name='brokerAgency_contact',
        ),
        migrations.RemoveField(
            model_name='checklist',
            name='brokerAgency_name',
        ),
        migrations.RemoveField(
            model_name='checklist',
            name='checklist_is_private',
        ),
        migrations.RemoveField(
            model_name='checklist',
            name='detailInfo',
        ),
        migrations.RemoveField(
            model_name='checklist',
            name='location_x',
        ),
        migrations.RemoveField(
            model_name='checklist',
            name='location_y',
        ),
        migrations.RemoveField(
            model_name='checklist',
            name='option',
        ),
        migrations.RemoveField(
            model_name='image',
            name='basicInfo',
        ),
        migrations.RemoveField(
            model_name='room',
            name='basicInfo',
        ),
        migrations.RemoveField(
            model_name='room',
            name='location_x',
        ),
        migrations.RemoveField(
            model_name='room',
            name='location_y',
        ),
        migrations.RemoveField(
            model_name='room',
            name='options',
        ),
        migrations.RemoveField(
            model_name='room',
            name='room_update_dt',
        ),
        migrations.AddField(
            model_name='checklist',
            name='is_confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.RemoveField(
            model_name='room',
            name='brokerAgency',
        ),
        migrations.AddField(
            model_name='room',
            name='brokerAgency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.brokeragency'),
        ),
        migrations.AlterField(
            model_name='room',
            name='tag',
            field=models.ManyToManyField(to='app.tag'),
        ),
        migrations.DeleteModel(
            name='BasicInfo',
        ),
        migrations.DeleteModel(
            name='ConfirmedRoom',
        ),
        migrations.DeleteModel(
            name='DetailInfo',
        ),
        migrations.DeleteModel(
            name='Option',
        ),
        migrations.AddField(
            model_name='image',
            name='roomInfo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.roominfo'),
        ),
        migrations.AddField(
            model_name='room',
            name='roomInfo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.roominfo'),
        ),
    ]
