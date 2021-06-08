#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method
from gnr.core.gnrbag import Bag
from imdb import IMDb

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('nome')
        r.fieldcell('cognome')
        r.fieldcell('nickname')
        r.fieldcell('data_nascita')
        r.fieldcell('provincia')
        r.fieldcell('email', width='auto')
        r.fieldcell('generi_preferiti')
        r.fieldcell('film_id')
        r.fieldcell('user_id')

    def th_order(self):
        return 'nome'

    def th_query(self):
        return dict(column='nome', op='contains', val='')



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
        fb.field('film_id', tag='remoteSelect', method = self.imdb_getMovieId, auxColumns='title,kind,year')
        fb.field('generi_preferiti', tag='checkboxtext', colspan=2, table='cine.genere', cols=2, popup=True)
        fb.field('bio', colspan=2, height='40px')

        center = bc.contentPane(region='center')
        center.dialogTableHandler(relation='@recensioni')

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')

    @public_method
    def imdb_getMovieId(self,_querystring=None,**kwargs):
        ia = IMDb()
        result = Bag()
        movies = ia.search_movie(_querystring)
        for movie in movies:
            movie_id = movie.movieID
            title=movie.get('title')
            year=movie.get('year')
            result.addItem(movie_id, None, title = title, year = str(year),
                                kind=movie.get('kind'), cover=movie.get('full-size cover url'), 
                                _pkey=movie_id, caption='{title} ({year})'.format(title=title, year=year))
        return result,dict(columns='title,kind,year', headers='Title,Kind,Year')

