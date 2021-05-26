# Generated by Django 3.2.3 on 2021-05-26 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NumBed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_bed', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_room', models.CharField(db_index=True, max_length=90)),
                ('description_room', models.TextField()),
                ('reservation', models.BooleanField()),
                ('free_date', models.DateField()),
                ('num_bed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.numbed')),
            ],
        ),
    ]