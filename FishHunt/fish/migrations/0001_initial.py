# Generated by Django 4.1.7 on 2023-03-31 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('date', models.DateField(auto_now=True)),
                ('image', models.ImageField(upload_to='assets/images')),
            ],
            options={
                'verbose_name': 'fish',
                'verbose_name_plural': 'fishes',
            },
        ),
    ]