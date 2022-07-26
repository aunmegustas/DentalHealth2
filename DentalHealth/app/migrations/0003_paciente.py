# Generated by Django 4.0.6 on 2022-07-26 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_clinica_cuenta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('edad', models.CharField(max_length=2)),
                ('direccion', models.CharField(max_length=45)),
                ('idcuenta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.cuenta')),
            ],
        ),
    ]
