from gnr.core.gnrdecorator import public_method
from gnr.core.gnrbag import Bag

class Table(object):
    def config_db(self,pkg):
        tbl = pkg.table('person', pkey='imdb_id', 
                        name_long='Person', 
                        name_plural='People', caption_field='person_name')
        self.sysFields(tbl)
        tbl.column('imdb_id', size='7', name_long='Film')
        tbl.column('person_name', name_long='Person name')