# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Donation.color'
        db.alter_column('donate_donation', 'color', self.gf('django.db.models.fields.CharField')(max_length=50))

    def backwards(self, orm):

        # Changing field 'Donation.color'
        db.alter_column('donate_donation', 'color', self.gf('django.db.models.fields.CharField')(max_length=20))

    models = {
        'donate.donation': {
            'Meta': {'object_name': 'Donation'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'amount_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'anchor': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
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