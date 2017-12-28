import webbrowser


class Video:
    """Video class which contains some attributes like title, poster image and
    trailler."""

    def __init__(self, title, year, duration, poster_image_url,
                 trailer_youtube_url):
        """Constructor method of Video class."""
        self.title = title
        self.year = year
        self.duration = duration
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """This method is responsible to open the web browser and show
        the content."""
        webbrowser.open(self.trailer_youtube_url)


class Movie(Video):
    def __init__(self, title, year, duration, poster_image_url,
                 trailer_youtube_url, storyline):
        """Constructor method of Movie child class."""
        Video.__init__(self, title, year, duration, poster_image_url,
                       trailer_youtube_url)
        self.storyline = storyline
