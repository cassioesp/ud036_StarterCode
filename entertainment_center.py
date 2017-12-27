import fresh_tomatoes
import media

# Creating some movie instances.
fight_club = media.Movie("Fight Club",
                         "1999",
                         "139 min",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BMzFjMWNhYzQtYTIxNC00ZWQ1LThiOTItNWQyZmMxNDYyMjA5XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UX182_CR0,0,182,268_AL_.jpg",
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg",
                         "An insomniac office worker, looking for a way to change his life, crosses paths with a devil-may-care soap maker, forming an underground fight club that evolves into something much, much more.")

django_unchained = media.Movie("Django Unchained",
                               "1996",
                               "165 min",
                               "https://images-na.ssl-images-amazon.com/images/M/MV5BMjIyNTQ5NjQ1OV5BMl5BanBnXkFtZTcwODg1MDU4OA@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                               "https://www.youtube.com/watch?v=eUdM9vrCbow",
                               "With the help of a German bounty hunter, a freed slave sets out to rescue his wife from a brutal Mississippi plantation owner.")

the_shining = media.Movie("The Shining",
                          "1980",
                          "146 min",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BZWFlYmY2MGEtZjVkYS00YzU4LTg0YjQtYzY1ZGE3NTA5NGQxXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                          "https://www.youtube.com/watch?v=S014oGZiSdI",
                          "A family heads to an isolated hotel for the winter where an evil spiritual presence influences the father into violence, while his psychic son sees horrific forebodings from the past and of the future.")

reservoir_dogs = media.Movie("Reservoir Dogs",
                             "1992",
                             "159 min",
                             "https://images-na.ssl-images-amazon.com/images/M/MV5BZmExNmEwYWItYmQzOS00YjA5LTk2MjktZjEyZDE1Y2QxNjA1XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                             "https://www.youtube.com/watch?v=vayksn4Y93A",
                             "After a simple jewelry heist goes terribly wrong, the surviving criminals begin to suspect that one of them is a police informant.")

trainspotting = media.Movie("Trainspotting",
                            "1997",
                            "94 min",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BMzA5Zjc3ZTMtMmU5YS00YTMwLWI4MWUtYTU0YTVmNjVmODZhXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg",
                            "https://www.youtube.com/watch?v=JuneXaJIAmo",
                            "Renton, deeply immersed in the Edinburgh drug scene, tries to clean up and get out, despite the allure of the drugs and influence of friends.")

into_the_wild = media.Movie("Into the Wild",
                            "2007",
                            "148 min",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BMTAwNDEyODU1MjheQTJeQWpwZ15BbWU2MDc3NDQwNw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                            "https://www.youtube.com/watch?v=lwtZgBFKlzs",
                            "After graduating from Emory University, top student and athlete Christopher McCandless abandons his possessions, gives his entire $24,000 savings account to charity and hitchhikes to Alaska to live in the wilderness. Along the way, Christopher encounters a series of characters that shape his life.")

movies = [fight_club, django_unchained, the_shining, reservoir_dogs, trainspotting, into_the_wild]

fresh_tomatoes.open_movies_page(movies)
