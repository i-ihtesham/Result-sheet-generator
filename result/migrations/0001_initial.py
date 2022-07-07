# Generated by Django 2.1 on 2019-03-14 20:40

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarkSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateField(default=datetime.date.today)),
                ('date_to', models.DateField(default=datetime.date.today)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marksheets', to='course.Course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resultsheets', to='student.Student')),
            ],
        ),
        migrations.CreateModel(
            name='MarkSheetDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obtained_marks', models.IntegerField(default=0)),
                ('total_marks', models.IntegerField(default=0)),
                ('subject', models.CharField(max_length=100)),
                ('markSheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detail', to='result.MarkSheet')),
            ],
        ),
    ]
