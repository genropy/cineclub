# encoding: utf-8


class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('proiezione',pkey='id',name_long='Proiezione',name_plural='Proiezioni', caption_field='codice')
        self.sysFields(tbl)

        tbl.column('codice', size='6',name_long='Codice')
        tbl.column('data',dtype='D',name_long='Data')
        tbl.column('ora',dtype='H',name_long='Ora')
        tbl.column('film_id', name_long='Film preferito id').relation('film.imdb_id',
                                                                      relation_name='proiezioni')
        tbl.column('titolo',name_long='Titolo')
        tbl.column('socio_id',size='22',name_long='Socio proponente id').relation('socio.id',
                                                                                  mode='foreignkey',
                                                                                  relation_name='film_proposti')