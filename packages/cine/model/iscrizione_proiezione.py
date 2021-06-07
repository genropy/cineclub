# encoding: utf-8


class Table(object):
    
    def config_db(self, pkg):
        tbl =  pkg.table('iscrizione_proiezione',pkey='id',name_long='Iscrizione',name_plural='Iscrizioni', caption_field='id')
        self.sysFields(tbl)
        tbl.column('n_iscrizione', size='9')
        tbl.column('proiezione_id', size='22', name_long='Proiezione').relation('proiezione.id', relation_name='iscritti')
        tbl.column('socio_id', size='22',name_long='Iscritto').relation('socio.id',
                                                                        mode='foreignkey',
                                                                        relation_name='iscrizioni_proiezioni')