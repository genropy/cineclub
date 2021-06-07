# encoding: utf-8


class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('proiezione',pkey='id',name_long='Proiezione',name_plural='Proiezioni',caption_field='id')
        self.sysFields(tbl)
        tbl.column('data',dtype='D',name_long='Data')
        tbl.column('ora',dtype='DH',name_long='Ora')
        tbl.column('film_id', name_long='ID Film')
        tbl.column('film_titolo', name_long='Titolo film', name_short='Film')
        tbl.column('film_cover_url',  name_long='Url cover')
        tbl.column('film_metadata', dtype='X', name_long='Dati film')
        tbl.column('titolo',name_long='Titolo')
        tbl.column('socio_id',size='22',name_long='Socio proponente id')