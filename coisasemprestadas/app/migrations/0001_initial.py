# Generated by Django 2.2.5 on 2019-10-02 13:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coisa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100)),
                ('data_emprestimo', models.DateField()),
                ('data_devolucao', models.DateField()),
                ('contato_amigo', models.CharField(max_length=11)),
                ('retorno', models.CharField(choices=[('D', 'Devolvido'), ('N', 'Não-Devolvivo')], max_length=1)),
                ('registration', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'coisa',
                'verbose_name_plural': 'coisa',
                'ordering': ('item',),
            },
        ),
    ]
