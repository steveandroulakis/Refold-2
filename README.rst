 rewrite of the REFOLD protein refolding record database
=========================================================

Formerly at http://refold.med.monash.edu.au

Security concerns on the former php4-based site have spurred this rewrite.

**Notes:**


* Currently only a read-only view of some database information. No ability for users to add/edit data.
* Requires an SQL database to be pre-loaded (i.e. django syncdb doesn't work for a blank database). This is due to the old database being used to create the Django models.
* Dependencies: django and django-completion (https://github.com/coleifer/django-completion/zipball/0.2.1)
* Buildout config for auto-dependency loading is coming, plus a guide to loading the autocomplete indexes
