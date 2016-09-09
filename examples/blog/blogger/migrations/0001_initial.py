# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Author'
        db.create_table(u'blogger_author', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'blogger', ['Author'])

        # Adding model 'BlogPost'
        db.create_table(u'blogger_blogpost', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blogger.Author'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('post', self.gf('django.db.models.fields.TextField')()),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'blogger', ['BlogPost'])


    def backwards(self, orm):
        # Deleting model 'Author'
        db.delete_table(u'blogger_author')

        # Deleting model 'BlogPost'
        db.delete_table(u'blogger_blogpost')


    models = {
        u'blogger.author': {
            'Meta': {'object_name': 'Author'},
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