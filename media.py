import webbrowser


# Defining the Movie Class with it instance variables; title, storyline,
# poster and youtube trailer
class Movie():
    """Gives the Movie Class' Documentation"""
    # Initiaze the Movie class constructor with the instance variables
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # this Instance method shows the trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
