import webbrowser

#class movie takes in the paremeters of title, plot, poster_image_url, and trailer_youtube_url.
#These parameters are strings. 
class Movie():
    def __init__(self, title, plot, poster, trailer, ratings):
        self.title = title
        self.storyline = plot
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer
        self.valid_ratings = ratings
        

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
