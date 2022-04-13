# Generated by Django 4.0.2 on 2022-02-27 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=200)),
                ('password1', models.CharField(max_length=10)),
                ('password2', models.CharField(max_length=10)),
            ],
        ),
    ]