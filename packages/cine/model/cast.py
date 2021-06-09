from gnr.core.gnrdecorator import public_method
from gnr.core.gnrbag import Bag
from imdb import IMDb

class Table(object):
    def config_db(self,pkg):
        tbl = pkg.table('cast', pkey='id', 
                        name_long='Cast', 
                        name_plural='Cast', caption_field='titolo')
        self.sysFields(tbl)
        tbl.column('film_id', size='7', name_long='Film')
        tbl.column('person_id', size='7', name_long='Person')
        tbl.column('character_name', name_long='Character name')