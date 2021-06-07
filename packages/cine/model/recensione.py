# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl = pkg.table('recensione', pkey='id', 
                        name_long='Recensione', 
                        name_plural='Recensioni',
                        caption_field='caption')
        self.sysFields(tbl)
        tbl.column('socio_id', size='22', name_long='Socio id').relation('socio.id',
                                                                        mode='foreignkey',
                                                                        onDelete='cascade',
                                                                        relation_name='recensioni')
        tbl.column('testo_recensione', name_long='Testo recensione', name_short='Testo')
        tbl.column('titolo_recensione', name_long='Titolo recensione', name_short='Titolo')
        tbl.column('voto', dtype='I', name_long='Voto recensione')
        tbl.column('film_id', name_long='ID Film')
        tbl.column('film_titolo', name_long='Titolo film', name_short='Film')
        tbl.column('film_cover_url',  name_long='Url cover')
        tbl.column('film_metadata', dtype='X', name_long='Dati film')
        tbl.aliasColumn('recensore', '@socio_id.nickname', name_long='Nickname recensore', name_short='Recensore')
        tbl.formulaColumn('caption',"$film_titolo || ' ' || $recensore")
    
