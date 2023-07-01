# Generated by Django 4.2.1 on 2023-06-08 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pincode', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('account', models.CharField(max_length=100)),
                ('note', models.CharField(max_length=100)),
            ],
        ),
    ]