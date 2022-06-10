# Generated by Django 2.2 on 2022-06-06 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cal02',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('wavelength', models.IntegerField()),
                ('caldata', models.FloatField()),
            ],
            options={
                'db_table': 'tb_two',
            },
        ),
        migrations.CreateModel(
            name='Cal03',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('wavelength', models.IntegerField()),
                ('caldata', models.FloatField()),
            ],
            options={
                'db_table': 'tb_three',
            },
        ),
        migrations.CreateModel(
            name='Calhim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('wavelength', models.IntegerField()),
                ('diff', models.FloatField()),
                ('global_irr', models.FloatField()),
                ('direct', models.FloatField()),
                ('dg_radio', models.FloatField()),
            ],
            options={
                'db_table': 'tb_him',
            },
        ),
    ]
