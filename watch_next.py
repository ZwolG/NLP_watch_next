# imports
import spacy

# loading language model
nlp = spacy.load('en_core_web_md')


with open('movies.txt', 'r') as f:
    movies = f.readlines()

# movie string with title and description
model_movie = 'Planet Hulk :Will he save\
their world or destroy it? When the Hulk becomes too dangerous for the\
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a\
planet where the Hulk can live in peace. Unfortunately, Hulk land on the\
planet Sakaar where he is sold into slavery and trained as a gladiator.'

# spliting movie string to get title and description
model_description = model_movie.split(' :')[1]
model_title = model_movie.split(' :')[0]

# function that will calculate similarity between descriptions of two movies
def which_movie_next(model_description,despcription):
    model_description = nlp(model_description)
    similarity = nlp(despcription).similarity(model_description)
    return similarity

# list to store titles, similarites
titles_and_similarites = []



# loop to iterate ove the movie file data 
# and to calculate similarity between model movie and movie description from the file
for i, movie in enumerate(movies):
    movie_description = movie.split(' :')[1]
    movie_title = movie.split(' :')[0]
    resemblance = which_movie_next(model_description, movie_description)
    print(model_title, ' - ', movie_title, ':  ', resemblance)
    titles_and_similarites.append([resemblance, movie_title])
    

print(max(titles_and_similarites), 'Max')
