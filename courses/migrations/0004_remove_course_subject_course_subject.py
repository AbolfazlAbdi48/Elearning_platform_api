# Generated by Django 4.0.5 on 2022-06-24 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='subject',
        ),
        migrations.AddField(
            model_name='course',
            name='subject',
            field=models.ManyToManyField(related_name='courses', to='courses.subject', verbose_name='subject'),
        ),
    ]
