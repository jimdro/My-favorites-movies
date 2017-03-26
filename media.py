import webbrowser


# Below is our main class with all variable instances
class Movie():
    def __init__(self, movie_title,
                 movie_storyline,
                 poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
# Below is the function to open youtube trailers

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
