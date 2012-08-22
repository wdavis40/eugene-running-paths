# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'City.population'
        db.delete_column('paths_city', 'population')


    def backwards(self, orm):
        # Adding field 'City.population'
        db.add_column('paths_city', 'population',
                      self.gf('django.db.models.fields.CharField')(default='Nothing Here', max_length=30),
                      keep_default=False)


    models = {
        'paths.city': {
            'Meta': {'object_name': 'City'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
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