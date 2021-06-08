# encoding: utf-8
from gnr.core.gnrdecorator import public_method
from gnr.core.gnrbag import Bag
from imdb import IMDb

class Table(object):
    def config_db(self,pkg):
        tbl = pkg.table('film', pkey='imdb_id', 
                        name_long='Film', 
                        name_plural='Film', caption_field='titolo')
        self.sysFields(tbl, id=False)
        tbl.column('imdb_id', size='7', name_long='id IMDB')
        tbl.column('titolo', name_long='Titolo film', name_short='Titolo')
        tbl.column('cover_url',  name_long='Url cover')
        tbl.column('dati', dtype='X', name_long='Dati film')

    def insertMovie(self, movie_id):
        pass

    def isIndexed(self, movie_id):
        result = self.query(where='$imdb_id=:movie_id', movie_id=movie_id).fetch()
        return bool(result)