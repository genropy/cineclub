#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('imdb_id', width='10em')
        r.fieldcell('titolo', width='20em')
    #    r.fieldcell('dati_anno')
    #    r.fieldcell('dati_genere')
    #    r.fieldcell('dati_regista')
    #    r.fieldcell('dati_trama')

    def th_order(self):
        return 'titolo'

    def th_query(self):
        return dict(column='titolo', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer() 
        top = bc.borderContainer(region='top',datapath='.record', height='350px')
        top.contentPane(region='right', padding='10px').img(src='^.dati.full-size-cover-url',
                height='300px',
                width='220px',
                border='2px dotted silver',
                rounded=6,
                placeholder=True,
                upload_folder='site:film/cover',
                upload_filename='=#FORM.record.imdb_id')
        fb = top.contentPane(region='center').div(width='95%').formbuilder(cols=2, border_spacing='4px', 
                                                            fld_width='100%', colswidth='auto', width='100%')
        fb.field('imdb_id', readOnly=True)
        fb.field('titolo', readOnly=True)
    #    fb.field('dati_anno', readOnly=True)
    #    fb.field('dati_genere', readOnly=True)
    #    fb.field('dati_regista', readOnly=True)
    #    fb.field('dati_trama', readOnly=True)
        fb.tree(storepath='.dati', lbl='Altri dati film: ', colspan=2)

        center = bc.contentPane(region='center')
        center.dialogTableHandler(relation='@recensioni', addrow=False, delrow=False)

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
