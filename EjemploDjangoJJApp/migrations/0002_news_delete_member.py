# Generated by Django 5.0.6 on 2024-06-17 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EjemploDjangoJJApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=200)),
                ('date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]
