import fresh_tomatoes
import media

# list of my favorite movies with their respective information

# Finding Nemo: title, poster image, link to trailer
finding_nemo = media.Movie(
  "Finding Nemo",
  "https://vignette.wikia.nocookie.net/disney/images/8/89/Finding_Nemo_-_Poster.jpg/revision/latest?cb=20160317170204",  # NOQA
  "https://www.youtube.com/watch?v=wZdpNglLbt8")

# Avengers: Infinity War: title, poster image, link to trailer
avengers_infinity_war = media.Movie(
  "Avengers: Infinity War",
  "https://vignette.wikia.nocookie.net/marvelcinematicuniverse/images/c/ca/Avengers_Infinity_War_Imax_poster.jpg/revision/latest?cb=20180405170202",  # NOQA
  "https://www.youtube.com/watch?v=B65hW9YYY5A")

# The Incredibles: title, poster image, link to trailer
incredibles = media.Movie(
  "The Incredibles",
  "https://ia.media-imdb.com/images/M/MV5BMTY5OTU0OTc2NV5BMl5BanBnXkFtZTcwMzU4MDcyMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg",  # NOQA
  "https://www.youtube.com/watch?v=eZbzbC9285I")

# Spiderman:Homecoming: title, poster image, link to trailer
spiderman_homecoming = media.Movie(
  "Spider-man: Homecoming",
  "https://cdn.traileraddict.com/content/columbia-pictures/spiderman-homecoming-poster-6.jpg",  # NOQA
  "https://www.youtube.com/watch?v=U0D3AOldjMU")

# Aladdin: title, poster image, link to trailer
aladdin = media.Movie(
  "Aladdin",
  "http://t2.gstatic.com/images?q=tbn:ANd9GcSsSEOwh6rx0SSBgd5IHoAZMaU3jLtyxMfFbtfJFTjc-SYHsFQL",  # NOQA
  "https://www.youtube.com/watch?v=QapaqcDucmg")

# The Lion King: title, poster image, link to trailer
the_lion_king = media.Movie(
  "The Lion King",
  "https://img.auctiva.com/imgdata/7/9/9/4/6/1/webimg/918301242_o.jpg",  # NOQA
  "https://www.youtube.com/watch?v=4sj1MT05lAA")

# list movies contains the names of the movies which store their information

movies = [finding_nemo,
          avengers_infinity_war,
          incredibles,
          spiderman_homecoming,
          aladdin,
          the_lion_king]

# this opens the page showing all my favorite movies
fresh_tomatoes.open_movies_page(movies)
