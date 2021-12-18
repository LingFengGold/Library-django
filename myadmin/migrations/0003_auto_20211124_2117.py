# Generated by Django 3.2.9 on 2021-11-24 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0002_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='password_hash',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='password_salt',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='username',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orders',
            name='return_status',
            field=models.IntegerField(default=4),
        ),
    ]