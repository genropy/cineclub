# encoding: utf-8


class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('proiezione',pkey='id',name_long='Proiezione',name_plural='Proiezioni',caption_field='id')
        self.sysFields(tbl)
        tbl.column('data',dtype='D',name_long='Data')
        tbl.column('ora',dtype='DH',name_long='Ora')
        tbl.column('film_imdb_id',name_long='Film')
        tbl.column('film_metadata',dtype='X',name_long='Dati film')
        tbl.column('titolo',name_long='Titolo')
        tbl.column('proposto_da',size='22',name_long='Proposto da')