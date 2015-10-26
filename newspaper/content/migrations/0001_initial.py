# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500)),
                ('subtitle', models.CharField(max_length=500)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_name', models.CharField(max_length=500)),
                ('first_name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('content_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='content.Content')),
                ('text', models.TextField()),
            ],
            bases=('content.content',),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('content_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='content.Content')),
                ('path', models.FilePathField()),
            ],
            bases=('content.content',),
        ),
        migrations.AddField(
            model_name='contributor',
            name='content',
            field=models.ManyToManyField(related_name='contributor', to='content.Content'),
        ),
        migrations.AddField(
            model_name='content',
            name='contributors',
            field=models.ManyToManyField(related_name='content_contributor', to='content.Contributor'),
        ),
        migrations.AddField(
            model_name='image',
            name='content',
            field=models.ForeignKey(related_name='content_image', to='content.Content'),
        ),
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.ForeignKey(related_name='content_article', to='content.Content'),
        ),
    ]
