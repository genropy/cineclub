# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl = pkg.table('film', pkey='imdb_id', 
                        name_long='Film', 
                        name_plural='Film')
        self.sysFields(tbl, id=False)
        tbl.column('imdb_id', size='7', name_long='id IMDB')
        tbl.column('titolo', name_long='Titolo film', name_short='Film')
        tbl.column('cover_url',  name_long='Url cover')
        tbl.column('dati', dtype='X', name_long='Dati film')