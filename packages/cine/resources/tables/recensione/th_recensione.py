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
        r.fieldcell('testo_recensione', width='auto')
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
        r.fieldcell('testo_recensione')
        r.fieldcell('voto')
        r.fieldcell('titolo_film')

    def th_order(self):
        return '__ins_ts:d'

    def th_query(self):
        return dict(column='titolo_film', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, width='500px', border_spacing='4px', fld_width='100%')
        fb.field('film_id', tag='remoteSelect', method=self.db.table('cine.film').imdb_getMovieId, 
                    auxColumns='title,year', lbl='Titolo Film', colspan=2)
        fb.field('titolo_recensione', colspan=2)
        fb.field('testo_recensione', tag='simpleTextArea', height='200px', colspan=2)
        fb.field('voto', tag='horizontalSlider', minimum=1, maximum=10, discreteValues=19, intermediateChanges=True)
        fb.div('^.voto', width='2em')

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
