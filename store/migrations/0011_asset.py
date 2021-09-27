# Generated by Django 3.0.8 on 2021-09-26 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20210926_1110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('insurance', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True)),
                ('repairs', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True)),
                ('broken', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True)),
                ('feedback', models.TextField(max_length=100, unique=True)),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]