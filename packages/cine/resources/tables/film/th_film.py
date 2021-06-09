#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('imdb_id', width='10em')
        r.fieldcell('titolo', width='20em')
        r.fieldcell('anno')
        r.fieldcell('imdb_rating', width='9em')
        r.fieldcell('genere')
        r.fieldcell('regista')
        r.fieldcell('trama', width='auto')

    def th_order(self):
        return 'titolo'

    def th_query(self):
        return dict(column='titolo', op='contains', val='')

class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer() 
        top = bc.borderContainer(region='top',datapath='.record', height='310px')
        center = top.roundedGroup(region='center', title='Film')
        fb = center.div(margin='5px', width='90%').formbuilder(cols=2, border_spacing='4px', width='100%', fld_width='100%')
        fb.field('imdb_id', readOnly=True, colspan=2)
        fb.field('titolo', readOnly=True, colspan=2)
        fb.field('anno', readOnly=True, format='####', width='5em')
        fb.field('imdb_rating', readOnly=True, width='5em')
        fb.field('genere', readOnly=True, colspan=2)
        fb.field('regista', readOnly=True, colspan=2)

        right = top.borderContainer(region='right', width='500px')
        right.roundedGroup(region='center', title='Cast').quickGrid(value='^.cast')

        right.contentPane(region='right', width='230px').img(src='^.cover_url',
                height='300px',
                width='220px',
                border='2px dotted silver',
                rounded=6,
                placeholder=True,
                upload_folder='site:film/cover',
                upload_filename='=#FORM.record.imdb_id')
                
        center = bc.tabContainer(region='center')
        self.tramaBox(center.contentPane(title='Trama', datapath='.record', padding='5px'))
        self.grigliaRecensioni(center.contentPane(title='Recensioni', padding='5px'))
        self.grigliaLovers(center.contentPane(title='Lovers', padding='5px'))
        self.altriDati(center.contentPane(title='Altri dati', datapath='.record', padding='5px'))

    def tramaBox(self, pane):
        pane.div('^.trama')

    def grigliaRecensioni(self, pane):
        pane.dialogTableHandler(relation='@recensioni', addrow=False, delrow=False)

    def grigliaLovers(self, pane):
        pane.plainTableHandler(relation='@preferito_soci')

    def altriDati(self, pane):
        pane.tree(storepath='.dati')

    def th_options(self):
        return dict(defaultPrompt=dict(title="Nuovo Film", doSave=True, 
                            fields=[dict(value='^.imdb_id', lbl='Titolo', tag='remoteSelect', 
                                            method='_table.cine.film.imdb_getMovieId', 
                                            auxColumns='title,year')]))
