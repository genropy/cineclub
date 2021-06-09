#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('nome')
        r.fieldcell('cognome')
        r.fieldcell('nickname')
        r.fieldcell('data_nascita')
        r.fieldcell('provincia')
        r.fieldcell('email', width='15em')
        r.fieldcell('generi_preferiti')
        r.fieldcell('n_recensioni')
        r.fieldcell('film_id')
        #r.fieldcell('user_id')

    def th_order(self):
        return 'cognome'

    def th_query(self):
        return dict(column='cognome', op='contains', val='')

class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer() 
        top = bc.borderContainer(region='top',datapath='.record',height='180px')
        top.contentPane(region='right',padding='10px').img(src='^.immagine',
                crop_height='150px',
                crop_width='150px',
                crop_border='2px dotted silver',
                crop_rounded=6,edit=True,
                placeholder=True,
                upload_folder='site:socio/avatars',
                upload_filename='=#FORM.record.nickname')
        fb = top.contentPane(region='center').div(width='95%').formbuilder(cols=2, border_spacing='4px', 
                                                            fld_width='100%', colswidth='auto', width='100%')
        fb.field('nome')
        fb.field('cognome')
        fb.field('nickname')
        fb.field('data_nascita')
        fb.field('email')
        fb.field('provincia')
        fb.field('comune_id')
        fb.field('film_id', tag='remoteSelect', method = self.db.table('cine.film').imdb_getMovieId, auxColumns='title,year')
        fb.field('generi_preferiti', tag='checkboxtext', colspan=2, table='cine.genere', cols=2, popup=True)
        fb.field('bio', colspan=2, height='40px')

        center = bc.contentPane(region='center')
        center.dialogTableHandler(relation='@recensioni', viewResource='ViewFromSocio')

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')