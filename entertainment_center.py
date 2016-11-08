import fresh_tomatoes
import media

#list of movies and their associated posters and trailers
blade_runner = media.Movie("Blade Runner",
                   "In a future Los Angeles, escaped replicants are hunted down",
                        "https://upload.wikimedia.org/wikipedia/en/5/53/Blade_Runner_poster.jpg",
                        "https://www.youtube.com/watch?v=eogpIG53Cis")


star_wars = media.Movie("Star Wars",
                     "A long time ago in a galaxy far far away",
                     "https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",
                     "https://www.youtube.com/watch?v=vP_1T4ilm8M")

the_martian = media.Movie("The Martian",
                         "A botanist who is presumedto be dead on Mars must use his ingenuity to survive",
                          "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",
                          "https://www.youtube.com/watch?v=Ue4PCI0NamI")


forbidden_planet = media.Movie("Forbidden Planet",
                               "A spacecraft travels to the planet AltairIV to determine the fate of scientists sent there decades earlier.  They find only Dr Morbius and his daughter.",
                               "https://upload.wikimedia.org/wikipedia/commons/5/50/Forbiddenplanetposter.jpg",
                               "https://www.youtube.com/watch?v=xEj8bZo9IGA")
alien = media.Movie("Alien",
                          "A space horror film",
                          "https://upload.wikimedia.org/wikipedia/en/c/c3/Alien_movie_poster.jpg",
                           "https://www.youtube.com/watch?v=LjLamj-b0I8")
prometheus = media.Movie("Prometheus",
                                "The discovery of a clue to mankind's origins on Earth leads a team of explorers to the darkest parts of the univrse",
                                "https://upload.wikimedia.org/wikipedia/en/a/a3/Prometheusposterfixed.jpg",
                                "https://www.youtube.com/watch?v=sftuxbvGwiU")

plan_nine = media.Movie("Plan 9 From Outer Space",
                        "Has been called the worst movie ever made",
                        "https://upload.wikimedia.org/wikipedia/commons/8/89/Plan_nine_from_outer_space.jpg",
                        "https://www.youtube.com/watch?v=u2ukRYsYPmo")
thx = media.Movie("THX 1138",
                  "In 25th Century Los Angeles, a man and woman rebel against their rigidly controlled society",
                  "https://upload.wikimedia.org/wikipedia/en/5/56/THX1138.jpg",
                  "https://www.youtube.com/watch?v=4hLXOVCZr-8")
interstellar = media.Movie("Interstellar",
                           "Earth searches for a new home planet through a wormhole",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=0vxOhd4qlnA")
metropolis = media.Movie("Metropolis",
                         "A futuristic city where a utopia exists above a bleak underworld",
                         "https://upload.wikimedia.org/wikipedia/en/0/06/Metropolisposter.jpg",
                         "https://www.youtube.com/watch?v=ZSExdX0tds4")
a_clockwork_orange = media.Movie("A Clockwork Orange",
                                 "A dystopian future where Droogs get high at a milk bar and wreak ultraviolence",
                                 "https://upload.wikimedia.org/wikipedia/en/4/48/Clockwork_orangeA.jpg",
                                 "https://www.youtube.com/watch?v=xHFPi_3kc1U")
serenity = media.Movie("Serenity",
                       "A group of rebels travels the outskirts of space aboard their ship Serenity",
                       "https://upload.wikimedia.org/wikipedia/en/9/9e/Serenity_One_Sheet.jpg",
                       "ttps://www.youtube.com/watch?v=ZLv_GTmAbEE")
                       
                  
                         
#movies array
movies = [blade_runner, star_wars, the_martian, forbidden_planet, alien, prometheus, plan_nine, thx, interstellar, metropolis, a_clockwork_orange, serenity]
#open web page using function in fresh_tomatoes.py 
fresh_tomatoes.open_movies_page(movies)

