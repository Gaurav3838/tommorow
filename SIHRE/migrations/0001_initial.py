# Generated by Django 3.0.4 on 2020-07-24 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='result2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pateint_id', models.CharField(max_length=100)),
                ('patient_name', models.CharField(max_length=100)),
                ('output', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'result_ml',
            },
        ),
    ]
