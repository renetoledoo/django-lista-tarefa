# Generated by Django 5.1 on 2024-10-28 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250, verbose_name='nome')),
                ('prioridade', models.CharField(max_length=1, verbose_name='prioridade')),
                ('area', models.CharField(max_length=50, verbose_name='area')),
                ('status', models.CharField(max_length=50, verbose_name='status')),
            ],
        ),
    ]
