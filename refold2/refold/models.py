# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from django.contrib.auth.models import User #, Group
from django.db import models

class RefoldBaseModel(models.Model):

    class Meta:
        abstract = True

class Additive(RefoldBaseModel):
    additive_id = models.IntegerField(primary_key=True)
    additive = models.CharField(max_length=765)
    user_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'additive'

class Admin(RefoldBaseModel):
    unique_hits = models.IntegerField()
    class Meta:
        db_table = u'admin'

class Assay(RefoldBaseModel):
    assay_id = models.IntegerField(primary_key=True)
    assay = models.CharField(max_length=300)
    assay_short = models.CharField(max_length=45)
    measurement = models.CharField(max_length=765)
    user_id = models.IntegerField()
    class Meta:
        db_table = u'assay'

class CellDisruptMethod(RefoldBaseModel):
    cell_disrupt_method_id = models.IntegerField(primary_key=True)
    cell_disrupt_method = models.CharField(max_length=300, blank=True)
    user_id = models.IntegerField()
    class Meta:
        db_table = u'cell_disrupt_method'

class Chaperones(RefoldBaseModel):
    chaperones_id = models.IntegerField(primary_key=True)
    chaperones = models.CharField(max_length=765)
    user_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'chaperones'

class Comment(RefoldBaseModel):
    comment_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User)
    comment = models.TextField(blank=True)
    date_posted = models.DateTimeField(null=True, blank=True)
    subject = models.CharField(max_length=765)
    class Meta:
        db_table = u'comment'

class ConstructDomains(RefoldBaseModel):
    domain_id = models.IntegerField(primary_key=True)
    domain_name = models.CharField(max_length=765)
    class Meta:
        db_table = u'construct_domains'

class ConstructHasDomain(RefoldBaseModel):
    construct_id = models.IntegerField()
    domain_id = models.IntegerField()
    start = models.IntegerField()
    end = models.IntegerField()
    class Meta:
        db_table = u'construct_has_domain'

class Disulphides(RefoldBaseModel):
    disulphides_id = models.IntegerField(primary_key=True)
    disulphides = models.CharField(max_length=300, blank=True)
    user_id = models.IntegerField()
    class Meta:
        db_table = u'disulphides'

class Family(RefoldBaseModel):
    family_id = models.IntegerField(primary_key=True)
    family = models.CharField(unique=True, max_length=255)
    sunid_f = models.CharField(max_length=180, blank=True)
    hits = models.IntegerField()
    scop_class = models.CharField(max_length=300, blank=True)
    user_id = models.IntegerField()
    class Meta:
        db_table = u'family'

    def __unicode__(self):
        return self.family

class Fusion(RefoldBaseModel):
    fusion_id = models.IntegerField(primary_key=True)
    fusion = models.CharField(max_length=300, blank=True)
    user_id = models.IntegerField()
    class Meta:
        db_table = u'fusion'

    def __unicode__(self):
        return self.fusion

class Groupcomparisons(RefoldBaseModel):
    id = models.IntegerField(primary_key=True)
    groupid = models.IntegerField()
    userid = models.IntegerField()
    comment = models.TextField(blank=True)
    date_created = models.IntegerField()
    proteins = models.CharField(max_length=765)
    link = models.TextField(blank=True)
    class Meta:
        db_table = u'groupcomparisons'

class Groupnotepad(RefoldBaseModel):
    groupid = models.IntegerField(primary_key=True)
    contents = models.TextField(blank=True)
    class Meta:
        db_table = u'groupnotepad'

class Groups(RefoldBaseModel):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    creatorid = models.IntegerField()
    class Meta:
        db_table = u'groups'

class Groupsearches(RefoldBaseModel):
    id = models.IntegerField(primary_key=True)
    groupid = models.IntegerField()
    userid = models.IntegerField()
    keyword = models.CharField(max_length=765, blank=True)
    date_created = models.IntegerField()
    link = models.TextField(blank=True)
    class Meta:
        db_table = u'groupsearches'

class Groupusers(RefoldBaseModel):
    userid = models.IntegerField()
    groupid = models.IntegerField()
    class Meta:
        db_table = u'groupusers'

class Journal(RefoldBaseModel):
    journal_id = models.IntegerField(primary_key=True)
    journal = models.CharField(max_length=150)
    user_id = models.IntegerField()
    class Meta:
        db_table = u'journal'

class LyticAgent(RefoldBaseModel):
    lytic_agent_id = models.IntegerField(primary_key=True)
    lytic_agent = models.CharField(max_length=765)
    user_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'lytic_agent'

class MethodInduction(RefoldBaseModel):
    method_induction_id = models.IntegerField(primary_key=True)
    method_induction = models.CharField(max_length=765)
    user_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'method_induction'

class OligoState(RefoldBaseModel):
    oligo_state_id = models.IntegerField(primary_key=True)
    oligo_state = models.CharField(max_length=300, blank=True)
    user_id = models.IntegerField()
    class Meta:
        db_table = u'oligo_state'

class PrePurification(RefoldBaseModel):
    pre_purification_id = models.IntegerField(primary_key=True)
    pre_purification = models.CharField(max_length=300, blank=True)
    user_id = models.IntegerField()
    class Meta:
        db_table = u'pre_purification'

class ProjectAim(RefoldBaseModel):
    project_aim_id = models.IntegerField(primary_key=True)
    project_aim = models.CharField(max_length=765)
    user_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'project_aim'

class Protein(RefoldBaseModel):
    protein_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User)
    family = models.ForeignKey(Family)
    name = models.CharField(unique=True, max_length=255, blank=True)
    name_short = models.CharField(max_length=75)
    structure_notes = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    hits = models.IntegerField()
    class Meta:
        db_table = u'protein'

    def __unicode__(self):
        return self.name

class ProteinComment(RefoldBaseModel):
    protein = models.ForeignKey(Protein)
    comment = models.ForeignKey(Comment)
    class Meta:
        db_table = u'protein_comment'

class Pubmedfeed(RefoldBaseModel):
    id = models.IntegerField(primary_key=True)
    item = models.TextField()
    results = models.IntegerField(null=True, blank=True)
    timestamp = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'pubmedFeed'

class RedoxAgent(RefoldBaseModel):
    redox_agent_id = models.IntegerField(primary_key=True)
    redox_agent = models.CharField(max_length=300, blank=True)
    user_id = models.IntegerField()
    class Meta:
        db_table = u'redox_agent'

class RedoxConc(RefoldBaseModel):
    redox_conc_id = models.IntegerField(primary_key=True)
    refolding_id = models.IntegerField()
    redox_concentration = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'redox_conc'

class RefTechnique(RefoldBaseModel):
    ref_technique_id = models.IntegerField(primary_key=True)
    ref_technique = models.CharField(max_length=300, blank=True)
    user_id = models.IntegerField()
    class Meta:
        db_table = u'ref_technique'

class Refoldblogfeed(RefoldBaseModel):
    id = models.IntegerField(primary_key=True)
    item = models.TextField()
    class Meta:
        db_table = u'refoldBlogFeed'

class RefoldingAdditive(RefoldBaseModel):
    refolding_id = models.IntegerField(primary_key=True)
    additive_id = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'refolding_additive'

class RefoldingAssay(RefoldBaseModel):
    refolding_id = models.IntegerField(primary_key=True)
    assay_id = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'refolding_assay'

class RefoldingChaperones(RefoldBaseModel):
    refolding_id = models.IntegerField(primary_key=True)
    chaperones_id = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'refolding_chaperones'

class RefoldingProjectAim(RefoldBaseModel):
    refolding_id = models.IntegerField(primary_key=True)
    project_aim_id = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'refolding_project_aim'

class Report(RefoldBaseModel):
    report_id = models.IntegerField(primary_key=True)
    journal = models.ForeignKey(Journal)
    authors = models.CharField(max_length=765)
    year = models.IntegerField()
    title = models.CharField(max_length=765)
    volume = models.IntegerField()
    pages = models.CharField(max_length=45)
    pubmed = models.CharField(max_length=765, blank=True)
    notes = models.TextField(blank=True)
    user_id = models.IntegerField()
    class Meta:
        db_table = u'report'

class Species(RefoldBaseModel):
    species_id = models.IntegerField(primary_key=True)
    common_name = models.CharField(max_length=150)
    scientific_name = models.CharField(max_length=150, blank=True)
    user_id = models.IntegerField()
    class Meta:
        db_table = u'species'

    def __unicode__(self):
        return str(self.common_name)

class Homologue(RefoldBaseModel):
    homologue_id = models.IntegerField(primary_key=True)
    protein = models.ForeignKey(Protein)
    species = models.ForeignKey(Species)
    user_id = models.IntegerField()
    uniprot = models.CharField(max_length=45, blank=True)
    swiss_prot_trembl = models.CharField(max_length=45, blank=True)
    structure_solved = models.CharField(max_length=42)
    sunid_p = models.CharField(max_length=180, blank=True)
    notes = models.TextField(blank=True)
    hits = models.IntegerField()
    class Meta:
        db_table = u'homologue'

    def __unicode__(self):
        return str(self.protein) + ' ' + str(self.species)

class Construct(RefoldBaseModel):
    construct_id = models.IntegerField(primary_key=True)
    homologue = models.ForeignKey(Homologue)
    user = models.ForeignKey(User)
    disulphides = models.ForeignKey(Disulphides)
    oligo_state = models.ForeignKey(OligoState)
    chain_length = models.IntegerField(null=True, blank=True)
    pi = models.FloatField(null=True, db_column='pI', blank=True) # Field name made lowercase.
    mol_wt = models.FloatField()
    sequence = models.TextField()
    full_length = models.CharField(max_length=3)
    domain = models.TextField(blank=True)
    chimera = models.TextField(blank=True)
    variants = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    hits = models.IntegerField()
    class Meta:
        db_table = u'construct'


class RefoldingRecord(RefoldBaseModel):
    refolding_id = models.IntegerField(primary_key=True)
    exptype = models.CharField(max_length=51)
    solubilization_buffer = models.CharField(max_length=450)
    ref_technique = models.ForeignKey(RefTechnique)
    refolding_buffer = models.CharField(max_length=765)
    refolding_ph = models.FloatField()
    refolding_temp = models.FloatField()
    refolding_time = models.CharField(max_length=75, blank=True)
    protocol = models.TextField()
    notes = models.TextField(blank=True)
    enzymes = models.CharField(max_length=300, blank=True)
    refolding_yield = models.CharField(max_length=150, blank=True)
    pre_purification = models.ForeignKey(PrePurification)
    cell_disrupt_method = models.ForeignKey(CellDisruptMethod)
    wash_buffer = models.CharField(max_length=600)
    redox_agent = models.ForeignKey(RedoxAgent)
    protein_conc = models.CharField(max_length=150, blank=True)
    expression_host = models.CharField(max_length=75)
    expression_strain = models.CharField(max_length=75)
    expression_vector = models.CharField(max_length=75)
    expression_temp = models.FloatField(null=True, blank=True)
    expression_time = models.CharField(max_length=75)
    inducing_concentration = models.CharField(max_length=300, blank=True)
    tag_cleaved = models.CharField(max_length=18)
    od_wavelength = models.IntegerField(null=True, db_column='OD_WaveLength', blank=True) # Field name made lowercase.
    cell_density = models.CharField(max_length=75, blank=True)
    fusion = models.ForeignKey(Fusion)
    purity = models.CharField(max_length=150, blank=True)
    construct = models.ForeignKey(Construct)
    user = models.ForeignKey(User)
    report = models.ForeignKey(Report)
    date_created = models.DateField()
    last_updated = models.DateField(null=True, blank=True)
    solubility = models.CharField(max_length=30)
    published = models.IntegerField()
    hits = models.IntegerField()
    lytic_agent = models.ForeignKey(LyticAgent, null=True, blank=True)
    method_induction = models.ForeignKey(MethodInduction, null=True, blank=True)
    protein_exp = models.CharField(max_length=3)
    protein_dena = models.CharField(max_length=3)
    cell_density_od = models.CharField(max_length=300, blank=True)
    cell_density_equals = models.CharField(max_length=300, blank=True)
    expression_protocol = models.TextField(blank=True)
    expression_notes = models.CharField(max_length=300, blank=True)
    additives_concentration = models.CharField(max_length=300, blank=True)
    ref_num = models.CharField(max_length=30, blank=True)
    class Meta:
        db_table = u'refolding_record'

    def __unicode__(self):
        return str(self.refolding_id)

class RefoldingComment(RefoldBaseModel):
    refolding = models.ForeignKey(RefoldingRecord)
    comment = models.ForeignKey(Comment)
    class Meta:
        db_table = u'refolding_comment'

class ScopClass(RefoldBaseModel):
    scop_class_id = models.IntegerField(primary_key=True)
    scop_class = models.CharField(max_length=300, blank=True)
    user_id = models.IntegerField()
    class Meta:
        db_table = u'scop_class'

class User(RefoldBaseModel):
    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=150, blank=True)
    pwd = models.CharField(max_length=150, blank=True)
    email = models.CharField(max_length=300, blank=True)
    title = models.CharField(max_length=30, blank=True)
    name = models.CharField(max_length=450)
    website_url = models.CharField(max_length=765, blank=True)
    org_name = models.CharField(max_length=450, blank=True)
    user_type = models.IntegerField(null=True, blank=True)
    last_login = models.CharField(max_length=150, blank=True)
    last_ip = models.CharField(max_length=135, blank=True)
    org_url = models.CharField(max_length=765)
    show_email = models.IntegerField()
    bio = models.TextField()
    signature = models.CharField(max_length=765)
    address1 = models.CharField(max_length=765)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    phone = models.CharField(max_length=60)
    append_signature_to_comments = models.IntegerField()
    show_contact_info = models.IntegerField()
    address2 = models.CharField(max_length=765)
    active = models.IntegerField()
    joined = models.CharField(max_length=150)
    post_count = models.IntegerField()
    moderator_notification = models.CharField(max_length=3, blank=True)
    user_notification = models.CharField(max_length=3, blank=True)
    class Meta:
        db_table = u'user'

class UserActivation(RefoldBaseModel):
    activation_id = models.IntegerField(primary_key=True)
    activation_code = models.CharField(max_length=765)
    user = models.ForeignKey(User)
    user_pwd = models.CharField(max_length=765)
    class Meta:
        db_table = u'user_activation'

class UserOnline(RefoldBaseModel):
    timestamp = models.IntegerField()
    ip = models.CharField(max_length=120)
    file = models.CharField(max_length=765, db_column='FILE') # Field name made lowercase.
    user_id = models.IntegerField()
    user_index = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'user_online'
