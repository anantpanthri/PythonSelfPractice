import media
import fresh_tomatoes
class MovieEntertainment():
    toystory=media.Movie("ToyStory","A boy finds his toys are alive",
                         "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                         "https://www.youtube.com/watch?v=QW0sjQFpXTU&feature=youtu.be")
    Bahubali2 = media.Movie("Bahubali2", "1000 crore",
                            "https://upload.wikimedia.org/wikipedia/en/f/f9/Baahubali_the_Conclusion.jpg",
                            "https://www.youtube.com/watch?v=G62HrubdD6o")
    OnceuponatimeinMumbai = media.Movie("1st Movie", "100000",
                                        "https://upload.wikimedia.org/wikipedia/en/b/ba/Once_Upon_a_Time_in_Mumbaai.jpg",
                                        "https://www.youtube.com/watch?v=LORrE6VN4E8")
    Bahubali = media.Movie("Bahubali", "1000 crore",
                           "https://upload.wikimedia.org/wikipedia/en/7/7e/Baahubali_poster.jpg",
                           "https://www.youtube.com/watch?v=sw6VKIClRMY")
    Avengers = media.Movie("Avenger", "1000 milllions",
                           "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
                           "https://www.youtube.com/watch?v=hIR8Ar-Z4hw")
    Spiderman = media.Movie("SuperVixen", "Pure Entertainment",
                           "https://upload.wikimedia.org/wikipedia/en/0/0c/Spiderman50.jpg",
                           "https://www.youtube.com/watch?v=bQ3nBSTpq4M")



    movies=[toystory,Bahubali2,OnceuponatimeinMumbai,Bahubali,Avengers,Spiderman]
    fresh_tomatoes.open_movies_page(movies)