# Generated by Django 3.2 on 2021-05-28 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('group_name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('responsibilities', models.TextField(blank=True, null=True)),
                ('established_on', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Miss', 'Miss'), ('Pastor', 'Pastor'), ('Reverend', 'Reverend'), ('Minister', 'Minister'), ('Presbyter', 'Presbyter'), ('Presbyteress', 'Presbyteress')], max_length=20)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('other_names', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('date_of_birth', models.DateField()),
                ('day_of_birth', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=10)),
                ('place_of_birth', models.CharField(blank=True, max_length=255, null=True)),
                ('hometown', models.CharField(blank=True, max_length=255, null=True)),
                ('nationality', models.CharField(default='Ghanaian', max_length=255)),
                ('profile_pic', models.FileField(upload_to='')),
                ('telephone', models.PositiveIntegerField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('working', models.BooleanField()),
                ('occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('schooling', models.BooleanField()),
                ('school', models.CharField(blank=True, max_length=255, null=True)),
                ('fathers_name', models.CharField(blank=True, max_length=255, null=True)),
                ('mothers_name', models.CharField(blank=True, max_length=255, null=True)),
                ('guardians_name', models.CharField(blank=True, max_length=255, null=True)),
                ('baptized', models.BooleanField()),
                ('baptism_date', models.DateField(blank=True, null=True)),
                ('confirmed', models.BooleanField()),
                ('confirmation_date', models.DateField(blank=True, null=True)),
                ('confirmation_church', models.CharField(blank=True, max_length=255, null=True)),
                ('new_believer_school', models.BooleanField()),
                ('active', models.BooleanField()),
                ('pays_tithe', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ministry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ministry', models.CharField(choices=[('Adult', 'Adult'), ('Youth', 'Youth'), ('Young_Adults', 'Young_Adults'), ('Children', 'Children'), ('Other', 'Other')], default='Adult', max_length=15)),
                ('remarks', models.CharField(blank=True, max_length=256)),
            ],
            options={
                'verbose_name_plural': 'ministries',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('role', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('responsibilities', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Miss', 'Miss'), ('Pastor', 'Pastor'), ('Reverend', 'Reverend'), ('Minister', 'Minister'), ('Presbyter', 'Presbyter'), ('Presbyteress', 'Presbyteress')], max_length=20)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('other_names', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('hometown', models.CharField(blank=True, max_length=255, null=True)),
                ('nationality', models.CharField(default='Ghanaian', max_length=255)),
                ('telephone', models.PositiveIntegerField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('working', models.BooleanField()),
                ('occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('schooling', models.BooleanField()),
                ('school', models.CharField(blank=True, max_length=255, null=True)),
                ('baptized', models.BooleanField()),
                ('confirmed', models.BooleanField()),
                ('confirmation_church', models.CharField(blank=True, max_length=255, null=True)),
                ('active', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
            ],
        ),
        migrations.CreateModel(
            name='Shepherd',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('membership_details', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='members.member')),
            ],
        ),
        migrations.CreateModel(
            name='MemberRole',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('group_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.group')),
                ('member_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.member')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.role')),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='ministry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='members.ministry'),
        ),
        migrations.AddField(
            model_name='group',
            name='group_members',
            field=models.ManyToManyField(to='members.Member'),
        ),
        migrations.CreateModel(
            name='Committee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('committe_name', models.CharField(max_length=255)),
                ('committee_leader', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('responsibilities', models.TextField()),
                ('designated_lifespan', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('committee_members', models.ManyToManyField(to='members.Member')),
            ],
        ),
    ]
