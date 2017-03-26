import fresh_tomatoes
import media

# Instance for Shawshank_redemption movie
shawshank_redemption = media.Movie("Shawshank Redemption",
                                   "A story of a prisoner by mistake",
                                   "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                                   "https://www.youtube.com/watch?v=6hB3S9bIaco")
print(shawshank_redemption.storyline)
# Instance for Ocean_11 movie
ocean_11 = media.Movie("Ocean 11",
                       "A team of gabmlers",
                       "https://upload.wikimedia.org/wikipedia/en/6/68/Ocean%27s_Eleven_2001_Poster.jpg",
                       "hhttps://www.youtube.com/watch?v=ImMGNQ2OEjo")
print(ocean_11.storyline)
# Instance for Lord_of_the_rings movie
lord_of_the_rings = media.Movie("Lord of the Rings", "The journey of destroying a ring",
                                "https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg",
                                "https://www.youtube.com/watch?v=V75dMMIW2B4")
print(lord_of_the_rings.storyline)
# Instance for School_of_rock
school_of_rock = media.Movie("School of Rock", "Using rock music to learn",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")
print(school_of_rock.storyline)
# Instance for X_men movie
x_men = media.Movie("X-men",
                    "A team of mutants",
                    "https://upload.wikimedia.org/wikipedia/en/0/04/X-Men_-_Apocalypse.jpg",
                    "https://www.youtube.com/watch?v=FAfR8omt-CY")
print(x_men.storyline)
# Instance for Batman movie
batman = media.Movie("Batman",
                     "Batman a fictional superhero",
                     "https://upload.wikimedia.org/wikipedia/en/2/22/Batman-DC-Comics.jpg",
                     "https://www.youtube.com/watch?v=mfmrPu43DF8")
print(batman.storyline)
# The list of the movies
movies = [shawshank_redemption, ocean_11,
          school_of_rock, x_men, batman, lord_of_the_rings]
# Calling the open_movie from fresh_tomatoes file
fresh_tomatoes.open_movies_page(movies)
