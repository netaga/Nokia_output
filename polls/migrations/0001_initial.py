# Generated by Django 3.2.5 on 2021-11-26 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Switches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('host', models.CharField(max_length=70)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(blank=True, max_length=100)),
                ('device_type', models.CharField(blank=True, choices=[('router', 'Router'), ('switch', 'Switch'), ('firewall', 'Firewall')], max_length=100)),
                ('platform', models.CharField(blank=True, choices=[('cisco_ios', 'cisco_IOS'), ('alcatel_aos', 'alcatel_AOS')], max_length=100)),
            ],
        ),
    ]