# Generated by Django 2.0.5 on 2018-07-04 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180704_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]