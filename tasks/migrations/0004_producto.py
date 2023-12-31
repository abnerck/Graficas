# Generated by Django 4.2.5 on 2023-09-15 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_remove_usuario_fecha_nacimiento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=50)),
                ('precioComun', models.IntegerField()),
                ('precioMayoreo', models.IntegerField()),
                ('canStock', models.IntegerField()),
                ('fechaingreso', models.DateTimeField()),
                ('tamaño', models.CharField(max_length=50)),
                ('material', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
            ],
        ),
    ]
