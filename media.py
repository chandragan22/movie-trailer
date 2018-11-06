import webbrowser

# class Movie stores movie information


class Movie():
    """
    Class Movie stores movie information
    """
    def __init__(self, movie_title, poster_image, trailer_youtube):
        """
        This constructor takes in the name of the movie,
        its poster image, and its trailer

        :param movie_title: string of movie title
        :param poster_image_url: string of poster image
        :param trailer_youtube_url: string of youtube url
        """
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        The show_trailer function takes the movie and
        displays its respective trailer in a
        """
        webbrowser.open(self.trailer_youtube_url)
