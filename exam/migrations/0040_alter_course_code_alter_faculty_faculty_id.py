# Generated by Django 5.1 on 2024-08-24 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0039_alter_student_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='code',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='faculty_id',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
