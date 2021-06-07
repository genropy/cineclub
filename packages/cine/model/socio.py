# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl = pkg.table('socio', pkey='id', name_long='Socio', name_plural='Soci', caption_field='nome_completo')
        self.sysFields(tbl)
        tbl.column('nome', size=':30', name_long='Nome')
        tbl.column('cognome', size='30', name_long='Cognome')
        tbl.column('nickname', size=':20', name_long='Nickname')    
        tbl.column('data_nascita', dtype='D', name_long='Data nascita')
        tbl.column('email', name_long='Email')
        tbl.column('provincia', name_long='Provincia').relation('glbl.provincia.sigla', 
                                                                mode='foreignkey',
                                                                relation_name='soci')
        tbl.column('comune_id', size='22', name_long='Comune id').relation('glbl.comune.id',
                                                            mode='foreignkey',
                                                            relation_name='soci')
        tbl.column('immagine', dtype='P', name_long='Immagine')
        tbl.column('generi_preferiti', name_long='Generi preferiti')
        tbl.column('bio', name_long='Bio')

        tbl.column('film_id', name_long='Film preferito id').relation('film.imdb_id',
                                                                      relation_name='preferito_soci')
        tbl.column('user_id',size='22', group='_', name_long='User').relation('adm.user.id',one_one=True, 
                                                                            relation_name='socio', 
                                                                            mode='foreignkey',
                                                                            onDelete='raise')
        tbl.aliasColumn('titolo_film_preferito', '@film_id.titolo', name_long='Titolo film preferito')
        tbl.formulaColumn('nome_completo',"$nome || ' ' || $cognome||'('||$nickname||')'")
    
