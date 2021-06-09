# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl = pkg.table('recensione', pkey='id', 
                        name_long='Recensione', 
                        name_plural='Recensioni',
                        caption_field='titolo_film')
        self.sysFields(tbl)
        tbl.column('socio_id', size='22', name_long='Socio id').relation('socio.id',
                                                                        mode='foreignkey',
                                                                        onDelete='cascade',
                                                                        relation_name='recensioni')
        tbl.column('testo_recensione', name_long='Testo recensione', name_short='Testo')
        tbl.column('titolo_recensione', name_long='Titolo recensione', name_short='Titolo')
        tbl.column('voto', dtype='I', name_long='Voto recensione', validate_notnull=True)
        tbl.column('film_id', name_long='ID Film').relation('film.imdb_id', relation_name='recensioni')
        tbl.aliasColumn('recensore', '@socio_id.nickname', name_long='Nickname recensore', name_short='Recensore')
        tbl.aliasColumn('titolo_film', '@film_id.titolo', name_long='Titolo Film', name_short='Film')

    def trigger_onInserting(self, record):
        if record.get('film_id'):
            self.cacheMovie(record)

    def cacheMovie(self, record):
        film_tbl = self.db.table('cine.film')
        if not film_tbl.isCached(record['film_id']):
            film_tbl.insertMovie(record['film_id'])

    def trigger_onUpdating(self, record, old_record):
        if record.get('film_id') and record.get('film_id')!=old_record.get('film_id'):
            self.cacheMovie(record)