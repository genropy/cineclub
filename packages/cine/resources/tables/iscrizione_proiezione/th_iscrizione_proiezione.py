#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('n_iscrizione')
        r.fieldcell('proiezione_id')
        r.fieldcell('socio_id')

    def th_order(self):
        return 'n_iscrizione'

    def th_query(self):
        return dict(column='n_iscrizione', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('n_iscrizione')
        fb.field('proiezione_id')
        fb.field('socio_id')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
