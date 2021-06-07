# encoding: utf-8


class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('genere', pkey='nome', name_long='Genere cinematografico', name_plural='Generi', caption_field='nome',lookup=True)
        tbl.column('nome',size=':20',name_long='Nome')
