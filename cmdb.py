import tmdbsimple as tmdb
import sys
import os

prompt = """ Connor Movie Database
1. Add Movie
2. Query Movie
3. Random Movie
4. Suggest Movie
"""

def add_movie():
    user_input = raw_input('Which movie do you want to add? ')
    search = tmdb.Search()
    response = search.movie(query=user_input)

    for movie in search.results:
        resp_prompt = 'Is this the correct movie? ' + movie['title'] + ', ' + \
                        movie['release_date'] + ' [y/n] '
        user_input = raw_input(resp_prompt)
        if user_input.lower() == 'y':
            print 'added! \n'
            return
    print 'Out of movies! Try again \n'

def add_to_db():
    pass

def query():
    print 'query'
    pass

def random():
    print 'random'
    pass

options = {
            '1'   : add_movie,
            'add' : add_movie,
            '2'     : query,
            'query' : query,
            '3'      : random,
            'random' : random,
}

if __name__ == '__main__':
    tmdb.API_KEY = os.environ['tmdb_key']
    user_input = 'start'
    print prompt
    while user_input != 'quit':
        user_input = raw_input('What would you like to do? ')
        san_input = user_input.lower()
        if san_input in options.keys():
            options[san_input]()
        else:
            print 'err'
