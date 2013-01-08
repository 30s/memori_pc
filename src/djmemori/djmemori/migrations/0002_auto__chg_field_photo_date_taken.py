# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Photo.date_taken'
        db.alter_column('djmemori_photo', 'date_taken', self.gf('django.db.models.fields.DateTimeField')())

    def backwards(self, orm):

        # Changing field 'Photo.date_taken'
        db.alter_column('djmemori_photo', 'date_taken', self.gf('django.db.models.fields.DateTimeField')(null=True))

    models = {
        'djmemori.photo': {
            'Meta': {'object_name': 'Photo'},
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(1970, 1, 1, 0, 0)'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'make': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'root': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['djmemori.ScanPath']"}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'djmemori.scanpath': {
            'Meta': {'object_name': 'ScanPath'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['djmemori']