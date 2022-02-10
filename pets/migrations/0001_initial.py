# Generated by Django 4.0.2 on 2022-02-07 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=15)),
                ('card', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('breed', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('color', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=200)),
                ('sold', models.BooleanField(default=False)),
                ('buyer', models.CharField(default='No buyer yet', max_length=30)),
                ('imageUrl', models.CharField(default='https://i.guim.co.uk/img/media/03734ee186eba543fb3d0e35db2a90a14a5d79e3/0_173_5200_3120/master/5200.jpg?width=1200&height=900&quality=85&auto=format&fit=crop&s=9c30ed97ea8731f3e2a155467201afe3', max_length=1000)),
            ],
        ),
    ]
