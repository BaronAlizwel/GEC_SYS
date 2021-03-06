# Generated by Django 3.2 on 2021-05-28 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(max_length=40, unique=True)),
                ('Remarks', models.CharField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(blank=True, max_length=255, null=True)),
                ('scriptures', models.CharField(blank=True, max_length=255, null=True)),
                ('groom_name', models.CharField(blank=True, max_length=255, null=True)),
                ('bride_name', models.CharField(blank=True, max_length=255, null=True)),
                ('invited_paster', models.CharField(blank=True, max_length=255, null=True)),
                ('event_date', models.DateField()),
                ('event_time_start', models.TimeField()),
                ('event_end_time', models.TimeField()),
                ('Remarks', models.CharField(blank=True, max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('service_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.eventtype')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adult_male', models.IntegerField(blank=True)),
                ('adult_female', models.IntegerField(blank=True)),
                ('youth_male', models.IntegerField(blank=True)),
                ('youth_female', models.IntegerField(blank=True)),
                ('young_adults_male', models.IntegerField(blank=True)),
                ('young_adults_female', models.IntegerField(blank=True)),
                ('children', models.IntegerField(blank=True)),
                ('total_male', models.IntegerField(default=0)),
                ('total_female', models.IntegerField(default=0)),
                ('total_attendance', models.IntegerField(default=0)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
            ],
            options={
                'verbose_name_plural': 'attendance',
            },
        ),
    ]
