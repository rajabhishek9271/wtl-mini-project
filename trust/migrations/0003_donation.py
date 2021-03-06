# Generated by Django 3.1 on 2021-01-23 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trust', '0002_volunteer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=100)),
                ('contact', models.BigIntegerField()),
                ('occupation', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('zipcode', models.BigIntegerField()),
                ('type', models.CharField(max_length=100)),
                ('amount', models.BigIntegerField(blank=True, null=True)),
            ],
        ),
    ]
