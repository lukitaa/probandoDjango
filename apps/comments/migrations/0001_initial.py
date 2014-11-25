# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comentario', models.CharField(max_length=100)),
                ('imagen', models.ImageField(upload_to=b'imagen_comentarios')),
                ('usuario', models.ManyToManyField(to='usuarios.Usuarios')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
