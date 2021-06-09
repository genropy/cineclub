#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('__ins_ts')
        r.fieldcell('recensore')
        r.fieldcell('titolo_recensione')
        r.fieldcell('voto')

    def th_order(self):
        return 'socio_id'

    def th_query(self):
        return dict(column='socio_id', op='contains', val='')

class ViewFromSocio(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('__ins_ts')
        r.fieldcell('titolo_recensione')
        r.fieldcell('voto')
        r.fieldcell('titolo_film')

    def th_order(self):
        return '__ins_ts:d'

    def th_query(self):
        return dict(column='titolo_film', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer()
        top = bc.contentPane(region='top')
        fb = top.formbuilder(cols=3,width='90%', border_spacing='4px', datapath='.record')
        fb.field('titolo_recensione', lbl='Titolo recensione', width='30em')
        fb.field('voto', lbl='Voto', validate_min=1,
                validate_max=10, width='3em',
                validate_max_error='Voto da 1 a 10',
                default=6)

        testo_box = bc.contentPane(region='center', datapath='.record').div( overflow='hidden')
        testo_box.ckeditor(value='^.testo_recensione')

    def th_options(self):
        return dict(dialog_parentRatio=.9, modal=True, defaultPrompt=dict(title="Nuova Recensione", doSave=True, 
                            fields=[dict(value='^.film_id', lbl='Film', tag='remoteSelect', 
                                            method='_table.cine.film.imdb_getMovieId', 
                                            auxColumns='title,year')]))
