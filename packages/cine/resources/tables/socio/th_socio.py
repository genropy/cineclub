#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('nome')
        r.fieldcell('cognome')
        r.fieldcell('nickname')
        r.fieldcell('data_nascita')
        r.fieldcell('email')
        r.fieldcell('provincia')
        r.fieldcell('comune_id')
        r.fieldcell('immagine')
        r.fieldcell('generi_preferiti')
        r.fieldcell('bio')
        r.fieldcell('film_id')
        r.fieldcell('user_id')

    def th_order(self):
        return 'nome'

    def th_query(self):
        return dict(column='nome', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        formbox = pane.div(width='90%')
        fb = formbox.formbuilder(cols=2, border_spacing='4px', fld_width='100%', colswidth='auto', width='100%')
        fb.field('nome')
        fb.field('cognome')
        fb.field('nickname')
        fb.field('immagine')
        fb.field('data_nascita')
        fb.field('email')
        fb.field('provincia')
        fb.field('comune_id')
        fb.field('generi_preferiti', tag='checkboxtext', colspan=2, table='cine.genere', cols=2, popup=True)
        fb.field('film_id', tag='remoteSelect', method = self.db.table('cine.film').getMovieId, 
                            auxColumns='title,kind,year')
        fb.field('bio', colspan=2)



    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
