#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('recensore')
        r.fieldcell('titolo_recensione')
        r.fieldcell('testo_recensione')
        r.fieldcell('voto')
        r.fieldcell('caption')

    def th_order(self):
        return 'socio_id'

    def th_query(self):
        return dict(column='socio_id', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('testo_recensione')
        fb.field('titolo_recensione')
        fb.field('voto')
        fb.field('film_id', tag='remoteSelect', method=self.db.table('cine.film').imdb_getMovieId, auxColumns='title,kind,year')
        fb.dataRpc(None, self.insertMovie, movie_id='^.film_id')

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
