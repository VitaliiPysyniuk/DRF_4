# Generated by Django 3.1.7 on 2021-03-14 23:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=30)),
                ('year', models.IntegerField()),
                ('price', models.IntegerField()),
                ('owner', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='cars', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'car',
            },
        ),
    ]