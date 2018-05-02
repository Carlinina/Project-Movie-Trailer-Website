import media
import fresh_tomatoes

amelie = media.Movie("Amelie",
                     "Amelie secretly executes complex schemes that affect the lives of those around her",
                     "https://upload.wikimedia.org/wikipedia/en/5/53/Amelie_poster.jpg",
                     "https://www.youtube.com/watch?v=HUECWi5pX7o")

star_wars = media.Movie("Star Wars",
                        "War in the space",
                        "https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg",
                        "https://www.youtube.com/watch?v=Q0CbN8sfihY")

life_is_beautiful = media.Movie("Life is Beautiful",
                             "Kids making music",
                             "https://upload.wikimedia.org/wikipedia/en/7/7c/Vitaebella.jpg",
                             "https://www.youtube.com/watch?v=4MpZyOdx4cs")

ratatouille = media.Movie("Ratatouille",
                          "A rat cooking",
                          "http://www.freemovieposters.net/posters/ratatouille_2007_681_poster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "Going back on time to meet authors",
                                "http://t2.gstatic.com/images?q=tbn:ANd9GcSUihv5aSDRTtjczvY5OVPe4pc-ByNoYf5QYQqYPV-C2tjCN45N",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

slumdog_millionaire = media.Movie("Slumdog Millionaire",
                                  "An indian muslim is one question away from the grand prize",
                                  "https://upload.wikimedia.org/wikipedia/en/9/92/Slumdog_Millionaire_poster.png",
                                  "https://www.youtube.com/watch?v=AIzbwV7on6Q")

movies = (amelie, star_wars, life_is_beautiful, ratatouille, midnight_in_paris, slumdog_millionaire)

fresh_tomatoes.open_movies_page(movies)

