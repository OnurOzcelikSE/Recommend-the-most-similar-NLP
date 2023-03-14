import spacy

def watch_next():
    # loads the md language model
    nlp = spacy.load("en_core_web_md")

    # description of the movie that user has already chosen / watched / liked
    planet_hulk = """Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, 
    the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. 
    Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."""

    # compares the movies, finds the similarity ratios
    compare = nlp(planet_hulk)

    # this dict keeps the movies in the movies.txt file and 
    # allows to sort them with the highest similarity rate to the movie that user watched
    recommendations = {} 

    # reads movies.txt file and turns the movies into a list
    with open("movies.txt", "r", encoding="utf-8") as movies:
        for movie in movies:

            # splits the movies and the descriptions
            line = movie.split(":")

            # calculates the similarity between the movie that user has chosen and the movies in the list 
            similarity = nlp(line[1]).similarity(compare) 

            # adds the similarity ratios to the dict
            recommendations[line[0]] = similarity

            # this print command shows the ratios of similarity if needed,
            # I prefer not to show it to the user for a clearer interface
            # print(line[0], similarity)

    # sorts the movies in the recommendations list by the order that user might like
    # 'reverse' makes the order descending 
    sort_recommendations = sorted(recommendations, key=recommendations.get, reverse=True)

    # prints out the result
    print("\nIf you liked this movie, you might also enjoy the ones listed below in the order listed:")
    for recommend in sort_recommendations:
        print(recommend)

# runs the function
watch_next()