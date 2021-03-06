# Generated by Django 3.0.8 on 2021-09-25 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20210925_2238'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('address', models.CharField(max_length=220)),
                ('phone', models.CharField(max_length=220, null=True)),
                ('location', models.CharField(max_length=120, unique=True)),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
