# Generated by Django 4.0.6 on 2022-08-09 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library_sys', '0001_initial'),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookitem',
            name='rack',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library_sys.rack'),
        ),
    ]