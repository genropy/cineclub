#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('imdb_id')
        r.fieldcell('titolo', width='auto')
        r.fieldcell('dati')

    def th_order(self):
        return 'imdb_id'

    def th_query(self):
        return dict(column='imdb_id', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer() 
        top = bc.borderContainer(region='top',datapath='.record',height='180px')
        top.contentPane(region='right',padding='10px').img(src='^.cover_url',
                crop_height='150px',
                crop_width='100px',
                crop_border='2px dotted silver',
                crop_rounded=6,edit=True,
                placeholder=True,
                upload_folder='site:film/cover',
                upload_filename='=#FORM.record.imdb_id')
        fb = top.contentPane(region='center').div(width='95%').formbuilder(cols=2, border_spacing='4px', 
                                                            fld_width='100%', colswidth='auto', width='100%')
        fb.field('imdb_id', readOnly=True)
        fb.field('titolo')
        fb.tree('^.dati', lbl='Dati film: ', colspan='2')

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
