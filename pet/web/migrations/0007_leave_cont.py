# Generated by Django 4.2.1 on 2023-06-12 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_contact_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='leave_cont',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=100)),
                ('Webiste', models.CharField(max_length=100)),
                ('Comment', models.CharField(max_length=100)),
            ],
        ),
    ]
