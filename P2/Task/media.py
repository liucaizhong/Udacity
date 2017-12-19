class Movie():
    '''This class is used to store movie related information.'''
    # definition of __init__
    def __init__(self, movie_title, poster_image, trailer_youku):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_url = trailer_youku
