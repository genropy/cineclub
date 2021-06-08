#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('codice')
        r.fieldcell('data')
        r.fieldcell('ora')
        r.fieldcell('film_id')
        r.fieldcell('titolo')
        r.fieldcell('socio_id')

    def th_order(self):
        return 'codice'

    def th_query(self):
        return dict(column='codice', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('codice')
        fb.field('data')
        fb.field('ora')
        fb.field('film_id')
        fb.field('titolo')
        fb.field('socio_id')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
