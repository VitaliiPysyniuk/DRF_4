# Generated by Django 3.1.7 on 2021-03-16 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'companies',
            },
        ),
    ]
