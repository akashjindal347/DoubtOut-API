# Generated by Django 2.2.1 on 2019-06-12 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100)),
                ('subject', models.CharField(choices=[('MATHS', 'MATHS'), ('SCIENCE', 'SCIENCE')], default='', max_length=10)),
            ],
        ),
    ]
