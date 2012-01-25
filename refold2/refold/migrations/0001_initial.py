# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Additive'
        db.create_table(u'additive', (
            ('additive_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('additive', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('refold', ['Additive'])

        # Adding model 'Admin'
        db.create_table(u'admin', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('unique_hits', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('refold', ['Admin'])

        # Adding model 'Assay'
        db.create_table(u'assay', (
            ('assay_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('assay', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('assay_short', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('measurement', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('refold', ['Assay'])

        # Adding model 'CellDisruptMethod'
        db.create_table(u'cell_disrupt_method', (
            ('cell_disrupt_method_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('cell_disrupt_method', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('refold', ['CellDisruptMethod'])

        # Adding model 'Chaperones'
        db.create_table(u'chaperones', (
            ('chaperones_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('chaperones', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('refold', ['Chaperones'])

        # Adding model 'Comment'
        db.create_table(u'comment', (
            ('comment_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('comment', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('date_posted', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=765)),
        ))
        db.send_create_signal('refold', ['Comment'])

        # Adding model 'ConstructDomains'
        db.create_table(u'construct_domains', (
            ('domain_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('domain_name', self.gf('django.db.models.fields.CharField')(max_length=765)),
        ))
        db.send_create_signal('refold', ['ConstructDomains'])

        # Adding model 'ConstructHasDomain'
        db.create_table(u'construct_has_domain', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('construct_id', self.gf('django.db.models.fields.IntegerField')()),
            ('domain_id', self.gf('django.db.models.fields.IntegerField')()),
            ('start', self.gf('django.db.models.fields.IntegerField')()),
            ('end', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('refold', ['ConstructHasDomain'])

        # Adding model 'Disulphides'
        db.create_table(u'disulphides', (
            ('disulphides_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('disulphides', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('refold', ['Disulphides'])

        # Adding model 'Family'
        db.create_table(u'family', (
            ('family_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('family', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('sunid_f', self.gf('django.db.models.fields.CharField')(max_length=180, blank=True)),
            ('hits', self.gf('django.db.models.fields.IntegerField')()),
            ('scop_class', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('refold', ['Family'])

        # Adding model 'Fusion'
        db.create_table(u'fusion', (
            ('fusion_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('fusion', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('refold', ['Fusion'])

        # Adding model 'Groupcomparisons'
        db.create_table(u'groupcomparisons', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('groupid', self.gf('django.db.models.fields.IntegerField')()),
            ('userid', self.gf('django.db.models.fields.IntegerField')()),
            ('comment', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('date_created', self.gf('django.db.models.fields.IntegerField')()),
            ('proteins', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('link', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('refold', ['Groupcomparisons'])

        # Adding model 'Groupnotepad'
        db.create_table(u'groupnotepad', (
            ('groupid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('contents', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('refold', ['Groupnotepad'])

        # Adding model 'Groups'
        db.create_table(u'groups', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('creatorid', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('refold', ['Groups'])

        # Adding model 'Groupsearches'
        db.create_table(u'groupsearches', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('groupid', self.gf('django.db.models.fields.IntegerField')()),
            ('userid', self.gf('django.db.models.fields.IntegerField')()),
            ('keyword', self.gf('django.db.models.fields.CharField')(max_length=765, blank=True)),
            ('date_created', self.gf('django.db.models.fields.IntegerField')()),
            ('link', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('refold', ['Groupsearches'])

        # Adding model 'Groupusers'
        db.create_table(u'groupusers', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('userid', self.gf('django.db.models.fields.IntegerField')()),
            ('groupid', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('refold', ['Groupusers'])

        # Adding model 'Journal'
        db.create_table(u'journal', (
            ('journal_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('journal', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('refold', ['Journal'])

        # Adding model 'LyticAgent'
        db.create_table(u'lytic_agent', (
            ('lytic_agent_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('lytic_agent', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('refold', ['LyticAgent'])

        # Adding model 'MethodInduction'
        db.create_table(u'method_induction', (
            ('method_induction_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('method_induction', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('refold', ['MethodInduction'])

        # Adding model 'OligoState'
        db.create_table(u'oligo_state', (
            ('oligo_state_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('oligo_state', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('refold', ['OligoState'])

        # Adding model 'PrePurification'
        db.create_table(u'pre_purification', (
            ('pre_purification_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('pre_purification', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('refold', ['PrePurification'])

        # Adding model 'ProjectAim'
        db.create_table(u'project_aim', (
            ('project_aim_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('project_aim', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('refold', ['ProjectAim'])

        # Adding model 'Protein'
        db.create_table(u'protein', (
            ('protein_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('family', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['refold.Family'])),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, blank=True)),
            ('name_short', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('structure_notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('hits', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('refold', ['Protein'])

        # Adding model 'ProteinComment'
        db.create_table(u'protein_comment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('protein', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['refold.Protein'])),
            ('comment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['refold.Comment'])),
        ))
        db.send_create_signal('refold', ['ProteinComment'])

        # Adding model 'Pubmedfeed'
        db.create_table(u'pubmedFeed', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('item', self.gf('django.db.models.fields.TextField')()),
            ('results', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('timestamp', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('refold', ['Pubmedfeed'])

        # Adding model 'RedoxAgent'
        db.create_table(u'redox_agent', (
            ('redox_agent_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('redox_agent', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('refold', ['RedoxAgent'])

        # Adding model 'RedoxConc'
        db.create_table(u'redox_conc', (
            ('redox_conc_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('refolding_id', self.gf('django.db.models.fields.IntegerField')()),
            ('redox_concentration', self.gf('django.db.models.fields.CharField')(max_length=765, blank=True)),
        ))
        db.send_create_signal('refold', ['RedoxConc'])

        # Adding model 'RefTechnique'
        db.create_table(u'ref_technique', (
            ('ref_technique_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('ref_technique', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('refold', ['RefTechnique'])

        # Adding model 'Refoldblogfeed'
        db.create_table(u'refoldBlogFeed', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('item', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('refold', ['Refoldblogfeed'])

        # Adding model 'RefoldingAdditive'
        db.create_table(u'refolding_additive', (
            ('refolding_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('additive_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
        ))
        db.send_create_signal('refold', ['RefoldingAdditive'])

        # Adding model 'RefoldingAssay'
        db.create_table(u'refolding_assay', (
            ('refolding_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('assay_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
        ))
        db.send_create_signal('refold', ['RefoldingAssay'])

        # Adding model 'RefoldingChaperones'
        db.create_table(u'refolding_chaperones', (
            ('refolding_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('chaperones_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
        ))
        db.send_create_signal('refold', ['RefoldingChaperones'])

        # Adding model 'RefoldingProjectAim'
        db.create_table(u'refolding_project_aim', (
            ('refolding_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('project_aim_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
        ))
        db.send_create_signal('refold', ['RefoldingProjectAim'])

        # Adding model 'Report'
        db.create_table(u'report', (
            ('report_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('journal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['refold.Journal'])),
            ('authors', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('volume', self.gf('django.db.models.fields.IntegerField')()),
            ('pages', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('pubmed', self.gf('django.db.models.fields.CharField')(max_length=765, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('refold', ['Report'])

        # Adding model 'Species'
        db.create_table(u'species', (
            ('species_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('common_name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('scientific_name', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('refold', ['Species'])

        # Adding model 'Homologue'
        db.create_table(u'homologue', (
            ('homologue_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('protein', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['refold.Protein'])),
            ('species', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['refold.Species'])),
            ('user_id', self.gf('django.db.models.fields.IntegerField')()),
            ('uniprot', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('swiss_prot_trembl', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('structure_solved', self.gf('django.db.models.fields.CharField')(max_length=42)),
            ('sunid_p', self.gf('django.db.models.fields.CharField')(max_length=180, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('hits', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('refold', ['Homologue'])

        # Adding model 'Construct'
        db.create_table(u'construct', (
            ('construct_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('homologue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['refold.Homologue'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('disulphides', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['refold.Disulphides'])),
            ('oligo_state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['refold.OligoState'])),
            ('chain_length', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pi', self.gf('django.db.models.fields.FloatField')(null=True, db_column='pI', blank=True)),
            ('mol_wt', self.gf('django.db.models.fields.FloatField')()),
            ('sequence', self.gf('django.db.models.fields.TextField')()),
            ('full_length', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('domain', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('chimera', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('variants', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('hits', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('refold', ['Construct'])

        # Adding model 'RefoldingRecord'
        db.create_table(u'refolding_record', (
            ('refolding_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('exptype', self.gf('django.db.models.fields.CharField')(max_length=51)),
            ('solubilization_buffer', self.gf('django.db.models.fields.CharField')(max_length=450)),
            ('ref_technique', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['refold.RefTechnique'])),
            ('refolding_buffer', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('refolding_ph', self.gf('django.db.models.fields.FloatField')()),
            ('refolding_temp', self.gf('django.db.models.fields.FloatField')()),
            ('refolding_time', self.gf('django.db.models.fields.CharField')(max_length=75, blank=True)),
            ('protocol', self.gf('django.db.models.fields.TextField')()),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('enzymes', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('refolding_yield', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('pre_purification', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['refold.PrePurification'])),
            ('cell_disrupt_method', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['refold.CellDisruptMethod'])),
            ('wash_buffer', self.gf('django.db.models.fields.CharField')(max_length=600)),
            ('redox_agent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['refold.RedoxAgent'])),
            ('protein_conc', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('expression_host', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('expression_strain', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('expression_vector', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('expression_temp', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('expression_time', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('inducing_concentration', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('tag_cleaved', self.gf('django.db.models.fields.CharField')(max_length=18)),
            ('od_wavelength', self.gf('django.db.models.fields.IntegerField')(null=True, db_column='OD_WaveLength', blank=True)),
            ('cell_density', self.gf('django.db.models.fields.CharField')(max_length=75, blank=True)),
            ('fusion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['refold.Fusion'])),
            ('purity', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('construct', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['refold.Construct'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('report', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['refold.Report'])),
            ('date_created', self.gf('django.db.models.fields.DateField')()),
            ('last_updated', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('solubility', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('published', self.gf('django.db.models.fields.IntegerField')()),
            ('hits', self.gf('django.db.models.fields.IntegerField')()),
            ('lytic_agent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['refold.LyticAgent'], null=True, blank=True)),
            ('method_induction', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['refold.MethodInduction'], null=True, blank=True)),
            ('protein_exp', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('protein_dena', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('cell_density_od', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('cell_density_equals', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('expression_protocol', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('expression_notes', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('additives_concentration', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('ref_num', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
        ))
        db.send_create_signal('refold', ['RefoldingRecord'])

        # Adding model 'RefoldingComment'
        db.create_table(u'refolding_comment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('refolding', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['refold.RefoldingRecord'])),
            ('comment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['refold.Comment'])),
        ))
        db.send_create_signal('refold', ['RefoldingComment'])

        # Adding model 'ScopClass'
        db.create_table(u'scop_class', (
            ('scop_class_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('scop_class', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('refold', ['ScopClass'])

        # Adding model 'User'
        db.create_table(u'user', (
            ('user_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('pwd', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=450)),
            ('website_url', self.gf('django.db.models.fields.CharField')(max_length=765, blank=True)),
            ('org_name', self.gf('django.db.models.fields.CharField')(max_length=450, blank=True)),
            ('user_type', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('last_login', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('last_ip', self.gf('django.db.models.fields.CharField')(max_length=135, blank=True)),
            ('org_url', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('show_email', self.gf('django.db.models.fields.IntegerField')()),
            ('bio', self.gf('django.db.models.fields.TextField')()),
            ('signature', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('address1', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('append_signature_to_comments', self.gf('django.db.models.fields.IntegerField')()),
            ('show_contact_info', self.gf('django.db.models.fields.IntegerField')()),
            ('address2', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('active', self.gf('django.db.models.fields.IntegerField')()),
            ('joined', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('post_count', self.gf('django.db.models.fields.IntegerField')()),
            ('moderator_notification', self.gf('django.db.models.fields.CharField')(max_length=3, blank=True)),
            ('user_notification', self.gf('django.db.models.fields.CharField')(max_length=3, blank=True)),
        ))
        db.send_create_signal('refold', ['User'])

        # Adding model 'UserActivation'
        db.create_table(u'user_activation', (
            ('activation_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('activation_code', self.gf('django.db.models.fields.CharField')(max_length=765)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['refold.User'])),
            ('user_pwd', self.gf('django.db.models.fields.CharField')(max_length=765)),
        ))
        db.send_create_signal('refold', ['UserActivation'])

        # Adding model 'UserOnline'
        db.create_table(u'user_online', (
            ('timestamp', self.gf('django.db.models.fields.IntegerField')()),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('file', self.gf('django.db.models.fields.CharField')(max_length=765, db_column='FILE')),
            ('user_id', self.gf('django.db.models.fields.IntegerField')()),
            ('user_index', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
        ))
        db.send_create_signal('refold', ['UserOnline'])


    def backwards(self, orm):
        
        # Deleting model 'Additive'
        db.delete_table(u'additive')

        # Deleting model 'Admin'
        db.delete_table(u'admin')

        # Deleting model 'Assay'
        db.delete_table(u'assay')

        # Deleting model 'CellDisruptMethod'
        db.delete_table(u'cell_disrupt_method')

        # Deleting model 'Chaperones'
        db.delete_table(u'chaperones')

        # Deleting model 'Comment'
        db.delete_table(u'comment')

        # Deleting model 'ConstructDomains'
        db.delete_table(u'construct_domains')

        # Deleting model 'ConstructHasDomain'
        db.delete_table(u'construct_has_domain')

        # Deleting model 'Disulphides'
        db.delete_table(u'disulphides')

        # Deleting model 'Family'
        db.delete_table(u'family')

        # Deleting model 'Fusion'
        db.delete_table(u'fusion')

        # Deleting model 'Groupcomparisons'
        db.delete_table(u'groupcomparisons')

        # Deleting model 'Groupnotepad'
        db.delete_table(u'groupnotepad')

        # Deleting model 'Groups'
        db.delete_table(u'groups')

        # Deleting model 'Groupsearches'
        db.delete_table(u'groupsearches')

        # Deleting model 'Groupusers'
        db.delete_table(u'groupusers')

        # Deleting model 'Journal'
        db.delete_table(u'journal')

        # Deleting model 'LyticAgent'
        db.delete_table(u'lytic_agent')

        # Deleting model 'MethodInduction'
        db.delete_table(u'method_induction')

        # Deleting model 'OligoState'
        db.delete_table(u'oligo_state')

        # Deleting model 'PrePurification'
        db.delete_table(u'pre_purification')

        # Deleting model 'ProjectAim'
        db.delete_table(u'project_aim')

        # Deleting model 'Protein'
        db.delete_table(u'protein')

        # Deleting model 'ProteinComment'
        db.delete_table(u'protein_comment')

        # Deleting model 'Pubmedfeed'
        db.delete_table(u'pubmedFeed')

        # Deleting model 'RedoxAgent'
        db.delete_table(u'redox_agent')

        # Deleting model 'RedoxConc'
        db.delete_table(u'redox_conc')

        # Deleting model 'RefTechnique'
        db.delete_table(u'ref_technique')

        # Deleting model 'Refoldblogfeed'
        db.delete_table(u'refoldBlogFeed')

        # Deleting model 'RefoldingAdditive'
        db.delete_table(u'refolding_additive')

        # Deleting model 'RefoldingAssay'
        db.delete_table(u'refolding_assay')

        # Deleting model 'RefoldingChaperones'
        db.delete_table(u'refolding_chaperones')

        # Deleting model 'RefoldingProjectAim'
        db.delete_table(u'refolding_project_aim')

        # Deleting model 'Report'
        db.delete_table(u'report')

        # Deleting model 'Species'
        db.delete_table(u'species')

        # Deleting model 'Homologue'
        db.delete_table(u'homologue')

        # Deleting model 'Construct'
        db.delete_table(u'construct')

        # Deleting model 'RefoldingRecord'
        db.delete_table(u'refolding_record')

        # Deleting model 'RefoldingComment'
        db.delete_table(u'refolding_comment')

        # Deleting model 'ScopClass'
        db.delete_table(u'scop_class')

        # Deleting model 'User'
        db.delete_table(u'user')

        # Deleting model 'UserActivation'
        db.delete_table(u'user_activation')

        # Deleting model 'UserOnline'
        db.delete_table(u'user_online')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
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
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
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
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
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
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
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
        'refold.user': {
            'Meta': {'object_name': 'User', 'db_table': "u'user'"},
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
        },
        'refold.useractivation': {
            'Meta': {'object_name': 'UserActivation', 'db_table': "u'user_activation'"},
            'activation_code': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'activation_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['refold.User']"}),
            'user_pwd': ('django.db.models.fields.CharField', [], {'max_length': '765'})
        },
        'refold.useronline': {
            'Meta': {'object_name': 'UserOnline', 'db_table': "u'user_online'"},
            'file': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'FILE'"}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'timestamp': ('django.db.models.fields.IntegerField', [], {}),
            'user_id': ('django.db.models.fields.IntegerField', [], {}),
            'user_index': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['refold']
