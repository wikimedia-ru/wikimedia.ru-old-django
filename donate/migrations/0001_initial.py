# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Donation'
        db.create_table('donate_donation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('icon', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('anchor', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('form_method', self.gf('django.db.models.fields.CharField')(default='get', max_length=4)),
            ('form_url', self.gf('django.db.models.fields.URLField')(max_length=250, null=True, blank=True)),
            ('phone_id', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('amount_id', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('submit_text', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('footnote', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('hidden', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('donate', ['Donation'])


    def backwards(self, orm):
        # Deleting model 'Donation'
        db.delete_table('donate_donation')


    models = {
        'donate.donation': {
            'Meta': {'object_name': 'Donation'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'amount_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'anchor': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'footnote': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'form_method': ('django.db.models.fields.CharField', [], {'default': "'get'", 'max_length': '4'}),
            'form_url': ('django.db.models.fields.URLField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'hidden': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'phone_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'submit_text': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['donate']