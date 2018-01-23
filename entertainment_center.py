import media
import fresh_tomatoes

trainspotting = media.Movie("Trainspotting",
                            "A story of a group of friends who are addicted to heroine.",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BMzA5Zjc3ZTMtMmU5YS00YTMwLWI4MWUtYTU0YTVmNjVmODZhXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_SX675_AL_.jpg",
                            "https://www.youtube.com/watch?v=8LuxOYIpu-I")
print trainspotting.storyline
#trainspotting.show_trailer()


the_basketball_diaries = media.Movie("The Basketball Diaries",
                                     "A story of a young man who gets addicted to drugs.",
                                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMjdlNzQxZGUtZTg5YS00ODg2LTkxMzctMDAyNmEwM2YyZjA4XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",
                                     "https://www.youtube.com/watch?v=NyfX9UHyxgY")
print the_basketball_diaries.storyline
#the_basketball_diaries.show_trailer()


requiem_for_a_dream = media.Movie("Requiem for a Dream",
                                  "A story of a group of people who are struggling with drugs and heroine.",
                                  "https://images-na.ssl-images-amazon.com/images/M/MV5BOTdiNzJlOWUtNWMwNS00NmFlLWI0YTEtZmI3YjIzZWUyY2Y3XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,666,1000_AL_.jpg",
                                  "https://www.youtube.com/watch?v=jzk-lmU4KZ4")
print requiem_for_a_dream.storyline
#requiem_for_a_dream.show_trailer()


mr_nobody = media.Movie("Mr Nobody",
                                  "A story of a man who is stucked with choices.",
                                  "https://images-na.ssl-images-amazon.com/images/M/MV5BMTg4ODkzMDQ3Nl5BMl5BanBnXkFtZTgwNTEwMTkxMDE@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                                  "https://www.youtube.com/watch?v=vXf3gVYXlHg")
print mr_nobody.storyline
#mr_nobody.show_trailer()


coach_carter = media.Movie("Coach Carter",
                                  "A story of a basketball team's great change with a help of their new coach. ",
                                  "https://images-na.ssl-images-amazon.com/images/M/MV5BNWYxZWFiNTItN2FkNS00ZDJmLWE1MWItYjMyMTgyOTI4MmQ4XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_SX675_AL_.jpg",
                                  "https://www.youtube.com/watch?v=znyAnWUYf2g")
print coach_carter.storyline
#coach_carter.show_trailer()


the_breakfast_club = media.Movie("The Breakfast Club",
                                  "A story of a group of high school students who spent their one day together for the first time. ",
                                  "https://images-na.ssl-images-amazon.com/images/M/MV5BOTM5N2ZmZTMtNjlmOS00YzlkLTk3YjEtNTU1ZmQ5OTdhODZhXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,639,1000_AL_.jpg",
                                  "https://www.youtube.com/watch?v=BSXBvor47Zs")
print the_breakfast_club.storyline
#the_breakfast_club.show_trailer()

movies = [trainspotting, the_basketball_diaries, requiem_for_a_dream, mr_nobody, coach_carter, the_breakfast_club] 
fresh_tomatoes.open_movies_page(movies)

