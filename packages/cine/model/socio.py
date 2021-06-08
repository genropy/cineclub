# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl = pkg.table('socio', pkey='id', name_long='Socio', name_plural='Soci', caption_field='nome_completo')
        self.sysFields(tbl)
        tbl.column('nome', size=':30', name_long='Nome', validate_notnull=True)
        tbl.column('cognome', size='30', name_long='Cognome', validate_notnull=True)
        tbl.column('nickname', size=':20', name_long='Nickname', validate_notnull=True, unique=True)    
        tbl.column('data_nascita', dtype='D', name_long='Data nascita')
        tbl.column('email', name_long='Email', validate_notnull=True)
        tbl.column('provincia', name_long='Provincia').relation('glbl.provincia.sigla', 
                                                                mode='foreignkey',
                                                                relation_name='soci')
        tbl.column('comune_id', size='22', name_long='Comune', name_short='Comune').relation('glbl.comune.id',
                                                            mode='foreignkey',
                                                            relation_name='soci')
        tbl.column('immagine', dtype='P', name_long='Immagine')
        tbl.column('generi_preferiti', name_long='Generi preferiti')
        tbl.column('bio', name_long='Bio')

        tbl.column('film_id', name_long='Film preferito').relation('film.imdb_id',
                                                                      relation_name='preferito_soci')
        tbl.column('user_id',size='22', group='_', name_long='User').relation('adm.user.id',one_one=True, 
                                                                            relation_name='socio', 
                                                                            mode='foreignkey',
                                                                            onDelete='raise')
        tbl.aliasColumn('titolo_film_preferito', '@film_id.titolo', name_long='Titolo film preferito')
        tbl.formulaColumn('nome_completo',"$nome || ' ' || $cognome||'('||$nickname||')'")
    

    def trigger_onInserting(self, record):
        pass

    def trigger_onUpdating(self, record, old_record):
        pass


