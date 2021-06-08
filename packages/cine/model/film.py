# encoding: utf-8
from gnr.core.gnrdecorator import public_method
from gnr.core.gnrbag import Bag
from imdb import IMDb

class Table(object):
    def config_db(self,pkg):
        tbl = pkg.table('film', pkey='imdb_id', 
                        name_long='Film', 
                        name_plural='Film', caption_field='titolo')
        self.sysFields(tbl, id=False)
        tbl.column('imdb_id', size='7', name_long='id IMDB')
        tbl.column('titolo', name_long='Titolo film', name_short='Titolo')
        tbl.column('dati', dtype='X', name_long='Dati film')

        tbl.bagItemColumn('dati_anno', dtype='T', bagcolumn='$dati', itempath='year', name_long='Anno')
        tbl.bagItemColumn('dati_genere', bagcolumn='$dati', itempath='kind', name_long='Genere')
        tbl.bagItemColumn('dati_regista', bagcolumn='$dati', itempath='directors.person.name', name_long='Regista')
        tbl.bagItemColumn('dati_trama', bagcolumn='$dati', itempath='plot-outline', name_long='Trama')

    def insertMovie(self, movie_id=None):
        ia = IMDb()
        movie = ia.get_movie(movie_id)
        movie_data = Bag(movie.asXML())['movie']
        rec = self.newrecord(imdb_id=movie_id, titolo=movie_data['title'], dati=movie_data)
        self.insert(rec)

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

    def isIndexed(self, movie_id):
        result = self.query(where='$imdb_id=:movie_id', movie_id=movie_id).fetch()
        return bool(result)