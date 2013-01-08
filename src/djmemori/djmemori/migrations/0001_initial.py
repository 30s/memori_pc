# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ScanPath'
        db.create_table('djmemori_scanpath', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('djmemori', ['ScanPath'])

        # Adding model 'Photo'
        db.create_table('djmemori_photo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('root', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['djmemori.ScanPath'])),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('date_taken', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('width', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('make', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('latitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('longitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('djmemori', ['Photo'])


    def backwards(self, orm):
        # Deleting model 'ScanPath'
        db.delete_table('djmemori_scanpath')

        # Deleting model 'Photo'
        db.delete_table('djmemori_photo')


    models = {
        'djmemori.photo': {
            'Meta': {'object_name': 'Photo'},
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
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