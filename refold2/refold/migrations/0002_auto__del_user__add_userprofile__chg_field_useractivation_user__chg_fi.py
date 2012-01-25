# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):

        # Adding model 'UserProfile'
        db.send_create_signal('refold', ['UserProfile'])

        # Changing field 'UserActivation.user'
        db.alter_column(u'user_activation', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['refold.UserProfile']))

        # Changing field 'Comment.user'
        db.alter_column(u'comment', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['refold.UserProfile']))

        # Changing field 'RefoldingRecord.user'
        db.alter_column(u'refolding_record', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['refold.UserProfile']))

        # Changing field 'Protein.user'
        db.alter_column(u'protein', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['refold.UserProfile']))

        # Changing field 'Construct.user'
        db.alter_column(u'construct', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['refold.UserProfile']))


    def backwards(self, orm):
        
        db.send_create_signal('refold', ['User'])

        # Changing field 'UserActivation.user'
        db.alter_column(u'user_activation', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['refold.User']))

        # Changing field 'Comment.user'
        db.alter_column(u'comment', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

        # Changing field 'RefoldingRecord.user'
        db.alter_column(u'refolding_record', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

        # Changing field 'Protein.user'
        db.alter_column(u'protein', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

        # Changing field 'Construct.user'
        db.alter_column(u'construct', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))


    models = {
        'refold.additive': {
            'Meta': {'object_name': 'Additive', 'db_table': "u'additive'"},
            'additive': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'additive_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'refold.admin': {
            'Meta': {'object_name': 'Admin', 'db_table': "u'admin'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'unique_hits': ('django.db.models.fields.IntegerField', [], {})
        },
        'refold.assay': {
            'Meta': {'object_name': 'Assay', 'db_table': "u'assay'"},
            'assay': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'assay_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'assay_short': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'measurement': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'refold.celldisruptmethod': {
            'Meta': {'object_name': 'CellDisruptMethod', 'db_table': "u'cell_disrupt_method'"},
            'cell_disrupt_method': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'cell_disrupt_method_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'refold.chaperones': {
            'Meta': {'object_name': 'Chaperones', 'db_table': "u'chaperones'"},
            'chaperones': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'chaperones_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'refold.comment': {
            'Meta': {'object_name': 'Comment', 'db_table': "u'comment'"},
            'comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'comment_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'date_posted': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['refold.UserProfile']"})
        },
        'refold.construct': {
            'Meta': {'object_name': 'Construct', 'db_table': "u'construct'"},
            'chain_length': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'chimera': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'construct_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'disulphides': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['refold.Disulphides']"}),
            'domain': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'full_length': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hits': ('django.db.models.fields.IntegerField', [], {}),
            'homologue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['refold.Homologue']"}),
            'mol_wt': ('django.db.models.fields.FloatField', [], {}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'oligo_state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['refold.OligoState']"}),
            'pi': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "'pI'", 'blank': 'True'}),
            'sequence': ('django.db.models.fields.TextField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['refold.UserProfile']"}),
            'variants': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'refold.constructdomains': {
            'Meta': {'object_name': 'ConstructDomains', 'db_table': "u'construct_domains'"},
            'domain_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'domain_name': ('django.db.models.fields.CharField', [], {'max_length': '765'})
        },
        'refold.constructhasdomain': {
            'Meta': {'object_name': 'ConstructHasDomain', 'db_table': "u'construct_has_domain'"},
            'construct_id': ('django.db.models.fields.IntegerField', [], {}),
            'domain_id': ('django.db.models.fields.IntegerField', [], {}),
            'end': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start': ('django.db.models.fields.IntegerField', [], {})
        },
        'refold.disulphides': {
            'Meta': {'object_name': 'Disulphides', 'db_table': "u'disulphides'"},
            'disulphides': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'disulphides_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'refold.family': {
            'Meta': {'object_name': 'Family', 'db_table': "u'family'"},
            'family': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'family_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'hits': ('django.db.models.fields.IntegerField', [], {}),
            'scop_class': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'sunid_f': ('django.db.models.fields.CharField', [], {'max_length': '180', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'refold.fusion': {
            'Meta': {'object_name': 'Fusion', 'db_table': "u'fusion'"},
            'fusion': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'fusion_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'refold.groupcomparisons': {
            'Meta': {'object_name': 'Groupcomparisons', 'db_table': "u'groupcomparisons'"},
            'comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date_created': ('django.db.models.fields.IntegerField', [], {}),
            'groupid': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'proteins': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'userid': ('django.db.models.fields.IntegerField', [], {})
        },
        'refold.groupnotepad': {
            'Meta': {'object_name': 'Groupnotepad', 'db_table': "u'groupnotepad'"},
            'contents': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'groupid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        'refold.groups': {
            'Meta': {'object_name': 'Groups', 'db_table': "u'groups'"},
            'creatorid': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '765'})
        },
        'refold.groupsearches': {
            'Meta': {'object_name': 'Groupsearches', 'db_table': "u'groupsearches'"},
            'date_created': ('django.db.models.fields.IntegerField', [], {}),
            'groupid': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'keyword': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'link': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'userid': ('django.db.models.fields.IntegerField', [], {})
        },
        'refold.groupusers': {
            'Meta': {'object_name': 'Groupusers', 'db_table': "u'groupusers'"},
            'groupid': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'userid': ('django.db.models.fields.IntegerField', [], {})
        },
        'refold.homologue': {
            'Meta': {'object_name': 'Homologue', 'db_table': "u'homologue'"},
            'hits': ('django.db.models.fields.IntegerField', [], {}),
            'homologue_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'protein': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['refold.Protein']"}),
            'species': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['refold.Species']"}),
            'structure_solved': ('django.db.models.fields.CharField', [], {'max_length': '42'}),
            'sunid_p': ('django.db.models.fields.CharField', [], {'max_length': '180', 'blank': 'True'}),
            'swiss_prot_trembl': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'uniprot': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'refold.journal': {
            'Meta': {'object_name': 'Journal', 'db_table': "u'journal'"},
            'journal': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'journal_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'refold.lyticagent': {
            'Meta': {'object_name': 'LyticAgent', 'db_table': "u'lytic_agent'"},
            'lytic_agent': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'lytic_agent_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'refold.methodinduction': {
            'Meta': {'object_name': 'MethodInduction', 'db_table': "u'method_induction'"},
            'method_induction': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'method_induction_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'refold.oligostate': {
            'Meta': {'object_name': 'OligoState', 'db_table': "u'oligo_state'"},
            'oligo_state': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'oligo_state_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'refold.prepurification': {
            'Meta': {'object_name': 'PrePurification', 'db_table': "u'pre_purification'"},
            'pre_purification': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'pre_purification_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'refold.projectaim': {
            'Meta': {'object_name': 'ProjectAim', 'db_table': "u'project_aim'"},
            'project_aim': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'project_aim_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'refold.protein': {
            'Meta': {'object_name': 'Protein', 'db_table': "u'protein'"},
            'family': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['refold.Family']"}),
            'hits': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'blank': 'True'}),
            'name_short': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'protein_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'structure_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['refold.UserProfile']"})
        },
        'refold.proteincomment': {
            'Meta': {'object_name': 'ProteinComment', 'db_table': "u'protein_comment'"},
            'comment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['refold.Comment']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'protein': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['refold.Protein']"})
        },
        'refold.pubmedfeed': {
            'Meta': {'object_name': 'Pubmedfeed', 'db_table': "u'pubmedFeed'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.TextField', [], {}),
            'results': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'refold.redoxagent': {
            'Meta': {'object_name': 'RedoxAgent', 'db_table': "u'redox_agent'"},
            'redox_agent': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'redox_agent_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'refold.redoxconc': {
            'Meta': {'object_name': 'RedoxConc', 'db_table': "u'redox_conc'"},
            'redox_conc_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'redox_concentration': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'refolding_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'refold.refoldblogfeed': {
            'Meta': {'object_name': 'Refoldblogfeed', 'db_table': "u'refoldBlogFeed'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.TextField', [], {})
        },
        'refold.refoldingadditive': {
            'Meta': {'object_name': 'RefoldingAdditive', 'db_table': "u'refolding_additive'"},
            'additive_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'refolding_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        'refold.refoldingassay': {
            'Meta': {'object_name': 'RefoldingAssay', 'db_table': "u'refolding_assay'"},
            'assay_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'refolding_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        'refold.refoldingchaperones': {
            'Meta': {'object_name': 'RefoldingChaperones', 'db_table': "u'refolding_chaperones'"},
            'chaperones_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'refolding_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        'refold.refoldingcomment': {
            'Meta': {'object_name': 'RefoldingComment', 'db_table': "u'refolding_comment'"},
            'comment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['refold.Comment']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'refolding': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['refold.RefoldingRecord']"})
        },
        'refold.refoldingprojectaim': {
            'Meta': {'object_name': 'RefoldingProjectAim', 'db_table': "u'refolding_project_aim'"},
            'project_aim_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'refolding_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        'refold.refoldingrecord': {
            'Meta': {'object_name': 'RefoldingRecord', 'db_table': "u'refolding_record'"},
            'additives_concentration': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'cell_density': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'}),
            'cell_density_equals': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'cell_density_od': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'cell_disrupt_method': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['refold.CellDisruptMethod']"}),
            'construct': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['refold.Construct']"}),
            'date_created': ('django.db.models.fields.DateField', [], {}),
            'enzymes': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'expression_host': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'expression_notes': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'expression_protocol': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expression_strain': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'expression_temp': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'expression_time': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'expression_vector': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'exptype': ('django.db.models.fields.CharField', [], {'max_length': '51'}),
            'fusion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['refold.Fusion']"}),
            'hits': ('django.db.models.fields.IntegerField', [], {}),
            'inducing_concentration': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'last_updated': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'lytic_agent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['refold.LyticAgent']", 'null': 'True', 'blank': 'True'}),
            'method_induction': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['refold.MethodInduction']", 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'od_wavelength': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'OD_WaveLength'", 'blank': 'True'}),
            'pre_purification': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['refold.PrePurification']"}),
            'protein_conc': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'protein_dena': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'protein_exp': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'protocol': ('django.db.models.fields.TextField', [], {}),
            'published': ('django.db.models.fields.IntegerField', [], {}),
            'purity': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'redox_agent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['refold.RedoxAgent']"}),
            'ref_num': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'ref_technique': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['refold.RefTechnique']"}),
            'refolding_buffer': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'refolding_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'refolding_ph': ('django.db.models.fields.FloatField', [], {}),
            'refolding_temp': ('django.db.models.fields.FloatField', [], {}),
            'refolding_time': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'}),
            'refolding_yield': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['refold.Report']"}),
            'solubility': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'solubilization_buffer': ('django.db.models.fields.CharField', [], {'max_length': '450'}),
            'tag_cleaved': ('django.db.models.fields.CharField', [], {'max_length': '18'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['refold.UserProfile']"}),
            'wash_buffer': ('django.db.models.fields.CharField', [], {'max_length': '600'})
        },
        'refold.reftechnique': {
            'Meta': {'object_name': 'RefTechnique', 'db_table': "u'ref_technique'"},
            'ref_technique': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'ref_technique_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'refold.report': {
            'Meta': {'object_name': 'Report', 'db_table': "u'report'"},
            'authors': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'journal': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['refold.Journal']"}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'pages': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'pubmed': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'report_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {}),
            'volume': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'refold.scopclass': {
            'Meta': {'object_name': 'ScopClass', 'db_table': "u'scop_class'"},
            'scop_class': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'scop_class_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'refold.species': {
            'Meta': {'object_name': 'Species', 'db_table': "u'species'"},
            'common_name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'scientific_name': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'species_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'refold.useractivation': {
            'Meta': {'object_name': 'UserActivation', 'db_table': "u'user_activation'"},
            'activation_code': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'activation_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['refold.UserProfile']"}),
            'user_pwd': ('django.db.models.fields.CharField', [], {'max_length': '765'})
        },
        'refold.useronline': {
            'Meta': {'object_name': 'UserOnline', 'db_table': "u'user_online'"},
            'file': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'FILE'"}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'timestamp': ('django.db.models.fields.IntegerField', [], {}),
            'user_id': ('django.db.models.fields.IntegerField', [], {}),
            'user_index': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        'refold.userprofile': {
            'Meta': {'object_name': 'UserProfile', 'db_table': "u'user'"},
            'active': ('django.db.models.fields.IntegerField', [], {}),
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'append_signature_to_comments': ('django.db.models.fields.IntegerField', [], {}),
            'bio': ('django.db.models.fields.TextField', [], {}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'joined': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'last_ip': ('django.db.models.fields.CharField', [], {'max_length': '135', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'moderator_notification': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '450'}),
            'org_name': ('django.db.models.fields.CharField', [], {'max_length': '450', 'blank': 'True'}),
            'org_url': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'post_count': ('django.db.models.fields.IntegerField', [], {}),
            'pwd': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'show_contact_info': ('django.db.models.fields.IntegerField', [], {}),
            'show_email': ('django.db.models.fields.IntegerField', [], {}),
            'signature': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'user_notification': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'user_type': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'website_url': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'})
        }
    }

    complete_apps = ['refold']
