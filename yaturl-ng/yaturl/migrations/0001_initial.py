# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Link'
        db.create_table('yaturl_link', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('link_shorthash', self.gf('django.db.models.fields.CharField')(unique=True, max_length=25)),
            ('link_hash', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=4096)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('entry_date', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('delete_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('yaturl', ['Link'])

        # Adding model 'Access'
        db.create_table('yaturl_access', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('link', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['yaturl.Link'])),
            ('access_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
        ))
        db.send_create_signal('yaturl', ['Access'])

        # Adding model 'BlockedLink'
        db.create_table('yaturl_blockedlink', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('link', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['yaturl.Link'], unique=True)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('entry_date', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
        ))
        db.send_create_signal('yaturl', ['BlockedLink'])


    def backwards(self, orm):
        # Deleting model 'Link'
        db.delete_table('yaturl_link')

        # Deleting model 'Access'
        db.delete_table('yaturl_access')

        # Deleting model 'BlockedLink'
        db.delete_table('yaturl_blockedlink')


    models = {
        'yaturl.access': {
            'Meta': {'object_name': 'Access'},
            'access_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['yaturl.Link']"})
        },
        'yaturl.blockedlink': {
            'Meta': {'object_name': 'BlockedLink'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'entry_date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['yaturl.Link']", 'unique': 'True'})
        },
        'yaturl.link': {
            'Meta': {'object_name': 'Link'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'delete_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'entry_date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '4096'}),
            'link_hash': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'link_shorthash': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '25'})
        }
    }

    complete_apps = ['yaturl']