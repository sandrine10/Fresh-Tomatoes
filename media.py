import webbrowser



class Movie():
    #This class provides a way to store movie related information

    def __init__(self, movie_title, movie_storyline, main_character, movie_rating, poster_image, video_info, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.main_character = main_character
        self.rating = movie_rating
        self.poster_image_url = poster_image
        self.video_info_url = video_info
        self.trailer_youtube_url = trailer_youtube
        # initialize instance of class Movie

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


