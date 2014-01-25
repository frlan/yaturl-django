# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Link.site'
        db.add_column('yaturl_link', 'site',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['sites.Site']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Link.site'
        db.delete_column('yaturl_link', 'site_id')


    models = {
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
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
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'delete_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'entry_date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '4096'}),
            'link_hash': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'link_shorthash': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '25'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"})
        }
    }

    complete_apps = ['yaturl']