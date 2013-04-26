# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'sdcr_app_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_type', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'sdcr_app', ['User'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'sdcr_app_user')


    models = {
        u'sdcr_app.user': {
            'Meta': {'object_name': 'User'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'user_type': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['sdcr_app']