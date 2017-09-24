import fresh_tomatoes
import media

#List of movies to be displayed on Movie site.
spirited_away = media.Movie('Spirited Away',
                            'A story of a girl who has to deal with the psychologically devastating event of seeing her parents turn into pigs. She then becomes friends/lovers with a dragon. Grade A stuff.',
                            'https://i.pinimg.com/736x/fe/3d/2d/fe3d2daa59dc0c6040677dfb87a1c15b--superhero-characters-alternative-movie-posters.jpg',
                            'https://www.youtube.com/watch?v=ByXuk9QqQkk',
                            'PG')

lotr_two_towers = media.Movie('The Two Towers',
                              'Some badass hobbits are trying to destory a ring that could be the destruction of all. Run little hobbits, run.',
                              'http://static.rogerebert.com/uploads/movie/movie_poster/lord-of-the-rings-the-two-towers-2002/large_9mBjBuUmBBgnGjV1JZ2uCIYbaph.jpg',
                              'https://www.youtube.com/watch?v=2dlRvAjU_RI',
                              'PG-13')

prometheus = media.Movie('Prometheus',
                         'Explorers are trying to find the origin of humankind while answering the question of the purpose of life. They then find out that their creators wanted to kill them. Sad juju.',
                         'http://t1.gstatic.com/images?q=tbn:ANd9GcR3blsaJx2hxJPhPCfLJA3knB4T8FUJtrvG-EIF9BTmtbIvXy02',
                         'https://www.youtube.com/watch?v=sftuxbvGwiU',
                         'R')

interstellar = media.Movie('Interstellar',
                           'The earth become inhabitable, so physicist want to transport humans to another planet to destroy that ecosystem. How are they going to do this? By travelling through a wormhole. Too bad they don\'t know which planets are inhabitable and Matt Damon tries to kill them.',
                           'http://t1.gstatic.com/images?q=tbn:ANd9GcRf61mker2o4KH3CbVE7Zw5B1-VogMH8LfZHEaq3UdCMLxARZAB',
                           'https://www.youtube.com/watch?v=0vxOhd4qlnA',
                           'PG-13')

requiem_dream = media.Movie('Requiem for a Dream',
                            'Stark view of human nature and addictions. Happy film. Not depressing at all. Just turn off your emotions and you will be fine! Directed by Aronofsky and music by the fantastic Clint Mansell. What could be better?',
                            'http://www.gstatic.com/tv/thumb/movieposters/25574/p25574_p_v8_ag.jpg',
                            'https://www.youtube.com/watch?v=jzk-lmU4KZ4',
                            'R')

magnolia = media.Movie('Magnolia',
                       'Another film about the complexities of human nature and how intertwined our lives can become. Another totally non-depressing film like Requiem.',
                       'http://www.gstatic.com/tv/thumb/movieposters/24393/p24393_p_v8_ae.jpg',
                       'https://www.youtube.com/watch?v=zwXDHSrNFbQ',
                       'R')

#put movies into an array to easily pass as a parameter to open_movies_page function.
movies = [requiem_dream, lotr_two_towers, spirited_away, prometheus, interstellar, magnolia]

#from the imported module fresh_tomatoes, call the method open_movies_page. Pass in the list of movies defined above.
#This will open a webbrowser display the list of the movies above and will allow the user to click on the movie
#in order to view the trailer. This will generate the HTML.
fresh_tomatoes.open_movies_page(movies)
