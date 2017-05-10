import webbrowser

class Movie():
    def __init__(self,title,story_line,poster,trailer):
        self.title=title
        self.story=story_line
        self.poster_image_url=poster
        self.trailer_youtube_url=trailer


    def showtrailer(self):
        webbrowser.open(self.trailer)