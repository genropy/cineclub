#!/usr/bin/env python
# encoding: utf-8
from gnr.app.gnrdbo import GnrDboTable, GnrDboPackage

class Package(GnrDboPackage):
    def config_attributes(self):
        return dict(comment='cine package',sqlschema='cine',sqlprefix=True,
                    name_short='Cine', name_long='Cineclub', name_full='Cine')
                    
    def config_db(self, pkg):
        pass
        
class Table(GnrDboTable):
    pass
