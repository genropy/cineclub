# -*- coding: utf-8 -*-

class GnrCustomWebPage(object):
    py_requires="gnrcomponents/testhandler:TestHandlerFull"

    def test_0_get_movie(self, pane, **kwargs):
        """Use remote select to connect with service and get results.
        Run pip install imdbpy first to retrieve movie data"""
        fb = pane.formbuilder(cols=1)
        fb.remoteSelect(value='^.movie_id',lbl='Movie title', method=self.db.table('cine.film').getMovieId, 
                            auxColumns='title,kind,year', selected_cover='.cover')
        fb.img(src='^.cover', hidden='^.cover?=!#v', width='200px', height='266px')
        fb.div('^.movie_id', lbl='Movie ID: ')