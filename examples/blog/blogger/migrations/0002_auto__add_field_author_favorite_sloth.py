# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Author.favorite_sloth'
        db.add_column(u'blogger_author', 'favorite_sloth',
                      self.gf('django.db.models.fields.CharField')(default='Punkin', max_length=128),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Author.favorite_sloth'
        db.delete_column(u'blogger_author', 'favorite_sloth')


    models = {
        u'blogger.author': {
            'Meta': {'object_name': 'Author'},
            'favorite_sloth': ('django.db.models.fields.CharField', [], {'default': "'Punkin'", 'max_length': '128'}),
            'first': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'blogger.blogpost': {
            'Meta': {'object_name': 'BlogPost'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blogger.Author']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post': ('django.db.models.fields.TextField', [], {}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        }
    }

    complete_apps = ['blogger']