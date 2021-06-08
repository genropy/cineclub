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
        tbl.column('cover_url', name_long='Cover url')
        tbl.column('anno', dtype='L', name_long='Anno')
        tbl.column('genere', name_long='Genere')
        tbl.column('regista', name_long='Regista')
        tbl.column('trama', name_long='Trama')
        tbl.column('cast', dtype='X', name_long='Cast')

    #    tbl.bagItemColumn('anno', dtype='L', bagcolumn='$dati', itempath='year', name_long='Anno')
    #    tbl.bagItemColumn('genere', bagcolumn='$dati', itempath='kind', name_long='Genere')
    #    tbl.bagItemColumn('regista', bagcolumn='$dati', itempath='directors.person.name', name_long='Regista')
    #    tbl.bagItemColumn('trama', bagcolumn='$dati', itempath='plot-outline', name_long='Trama')

    def imdb_getMovieData(self, movie_id=None):
        ia = IMDb()
        movie = ia.get_movie(movie_id)
        movie_data = Bag(movie.asXML())['movie']
        registi = ','.join(movie_data['directors'].digest('#v.name'))
        generi = ','.join(movie_data['genres'].digest('#v'))
        cast = self.preparaCast(cast=movie_data['cast'])
        movie_dict = dict(imdb_id=movie_id, titolo=movie_data['title'], cover_url=movie_data['full-size-cover-url'],
                                anno=movie_data['year'], genere=generi, cast=cast, 
                                regista=registi, trama=movie_data['plot-outline'], dati=movie_data)
        return movie_dict
    
    def preparaCast(self, cast=None):
        result=Bag()
        for person in cast.values():
            result.addItem('p', None, name=person['name'], character=person['current-role.character.name'])
        return result
        
    def insertMovie(self, movie_id=None):
        movie_rec = self.imdb_getMovieData(movie_id=movie_id)
        self.insert(movie_rec)

    @public_method
    def imdb_getMovieId(self,_querystring=None,**kwargs):
        ia = IMDb()
        result = Bag()
        movies = ia.search_movie(_querystring)
        for movie in movies:
            if movie.data['kind'] != 'movie':
                continue
            movie_id = movie.movieID
            title=movie.get('title')
            year=str(movie.get('year'))
            result.addItem(movie_id, None, title = title, year = year,
                                cover=movie.get('full-size cover url'), _pkey=movie_id, 
                                caption='{title} ({year})'.format(title=title, year=year))
        return result,dict(columns='title,year', headers='Title,Year')
    
    def isCached(self, movie_id):
        result = self.query(where='$imdb_id=:movie_id', movie_id=movie_id).fetch()
        return bool(result)

    def trigger_onInserting(self, record):
        record.update(self.imdb_getMovieData(record['imdb_id']))
