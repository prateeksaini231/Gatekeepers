# Generated by Django 3.0.2 on 2020-04-03 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visitors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('houseno', models.CharField(max_length=10)),
                ('purpose', models.CharField(max_length=10)),
                ('date_time', models.DateTimeField(verbose_name='visit_date_time')),
            ],
        ),
    ]
