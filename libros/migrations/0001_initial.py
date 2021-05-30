# Generated by Django 3.2.3 on 2021-05-30 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0003_autor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Título')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.autor', verbose_name='Autor')),
                ('categorias', models.ManyToManyField(to='core.Categoria', verbose_name='Categorías')),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
                'ordering': ['titulo'],
            },
        ),
    ]
