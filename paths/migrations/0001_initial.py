# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Path'
        db.create_table('paths_path', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['paths.City'])),
            ('state_province', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('paths', ['Path'])

        # Adding model 'City'
        db.create_table('paths_city', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('population', self.gf('django.db.models.fields.CharField')(default='Nothing Here', max_length=30)),
        ))
        db.send_create_signal('paths', ['City'])


    def backwards(self, orm):
        # Deleting model 'Path'
        db.delete_table('paths_path')

        # Deleting model 'City'
        db.delete_table('paths_city')


    models = {
        'paths.city': {
            'Meta': {'object_name': 'City'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'population': ('django.db.models.fields.CharField', [], {'default': "'Nothing Here'", 'max_length': '30'})
        },
        'paths.path': {
            'Meta': {'object_name': 'Path'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['paths.City']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'state_province': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['paths']