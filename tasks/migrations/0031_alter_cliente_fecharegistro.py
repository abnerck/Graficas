# Generated by Django 4.2.4 on 2023-10-09 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0030_alter_producto_fechaingreso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fecharegistro',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
