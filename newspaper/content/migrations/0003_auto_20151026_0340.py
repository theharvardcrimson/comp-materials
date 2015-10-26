# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20151020_1820'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('content_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='content.Content')),
            ],
            bases=('content.content',),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='content',
            field=models.ManyToManyField(related_name='contributor_content', to='content.Content'),
        ),
        migrations.AlterField(
            model_name='image',
            name='path',
            field=models.ImageField(upload_to=b'image_path'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='images',
            field=models.ManyToManyField(related_name='gallery_image', to='content.Image'),
        ),
    ]
