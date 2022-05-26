# Generated by Django 3.2.13 on 2022-05-23 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learnwithus', '0013_delete_joinedcourses'),
    ]

    operations = [
        migrations.CreateModel(
            name='JoinedCourses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.TextField()),
                ('profileid', models.PositiveIntegerField()),
                ('courseid', models.PositiveIntegerField()),
            ],
        ),
    ]
