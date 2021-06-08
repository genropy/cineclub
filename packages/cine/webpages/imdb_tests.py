# -*- coding: utf-8 -*-
from imdb import IMDb
from gnr.core.gnrdecorator import public_method
from gnr.core.gnrbag import Bag

class GnrCustomWebPage(object):
    py_requires="gnrcomponents/testhandler:TestHandlerFull"

    def test_0_get_movie(self, pane, **kwargs):
        """Use remote select to connect with service and get results.
        Run pip install imdbpy first to retrieve movie data"""
        fb = pane.formbuilder(cols=1)
        fb.remoteSelect(value='^.movie_id',lbl='Movie title', method=self.imdb_getMovieId, 
                            auxColumns='title,kind,year', selected_cover='.cover')
        fb.img(src='^.cover', hidden='^.cover?=!#v', width='200px', height='266px')
        fb.div('^.movie_id', lbl='Movie ID: ')

    @public_method
    def imdb_getMovieId(self,_querystring=None,**kwargs):
        ia = IMDb()
        result = Bag()
        movies = ia.search_movie(_querystring)
        for movie in movies:
            movie_id = movie.movieID
            title=movie.get('title')
            year=str(movie.get('year'))
            result.addItem(movie_id, None, title = title, year = year,
                                kind=movie.get('kind'), cover=movie.get('full-size cover url'), 
                                _pkey=movie_id, caption='{title} ({year})'.format(title=title, year=year))
        return result,dict(columns='title,kind,year', headers='Title,Kind,Year')

    def test_1_get_movieBag(self, pane, **kwargs):
        fb = pane.formbuilder(cols=1)
        fb.remoteSelect(value='^.movie_id',lbl='Movie title', method=self.imdb_getMovieId, auxColumns='title,kind,year')
        fb.dataRpc('.movie_data', self.getMovieData, movie_id='^.movie_id')
        fb.tree(storepath='.movie_data', lbl='Movie data: ')

    @public_method
    def getMovieData(self, movie_id=None):
        ia = IMDb()
        movie = ia.get_movie(movie_id)
        result = Bag(movie.asXML())['movie']
        return result