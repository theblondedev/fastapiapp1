# read input data
#analysis data and generate a profile.json file

#suitability for the below careers based on there selected questions

# <option value="ceo">CEO of large mega-corporation<br/>
# <option value="astronaut">Astronaut<br/>
# <option value="doctor">Medical doctor<br/>
# <option value="model">Fashion model<br/>
# <option value="rockstar">Rock star<br/>
# <option value="garbage">Refuse collection operative<br/>
#The result of actioning the /analyze URI should be the psychological profile data and image
#files stored at the server. These data should NOT be delivered to the client at this point.
#The server response should just be a simple message in a suitable format.
import json
import httpx


#dog uri



CAREER_RULES = {
    "ceo": ["question1", "question10", "question2", "question8"],
    "astronaut": ["question2", "question10", "question6", "question7"],
    "doctor": ["question4", "question10", "question2", "question20"],
    "model": ["question1", "question8", "question3"],
    "rockstar": ["question1", "question8", "question3"],
    "garbage": ["question4", "question8", "question10"]
}

MOVIE_RECOMMENDATIONS = {
    "ceo": ["Legally Blonde", "The Intern"],
    "astronaut": ["Apollo 13", "The Martian"],
    "doctor": ["The Theory Of Everything", "My Sister's Keeper"],
    "model": ["13 Going on 30", "Confessions of a teenage drama queen"],
    "rockstar": ["School of Rock", "A Complete Unknown"],
    "garbage": ["The Maid", "Cleaner"]
}


def score_answer(value):
    if value >= 4:
        return 2
    elif value == 3:
        return 1
    else:
        return 0

def get_movie(title):
    url = f"http://www.omdbapi.com/?apikey=e2b5cd8d&t={title}"
    response = httpx.get(url)
    response.raise_for_status()
    return response.json()


def run_analysis():
    with open("data/input.json") as f:
        data = json.load(f)

    career = data.get("job")

    score = 0
    for question in CAREER_RULES.get(career, []):
        value = data.get(question, 0)
        score += score_answer(value)

    result = {
        "career": career,
        "score": score,
        "answers questions": {q: data.get(q, 0) for q in CAREER_RULES.get(career, [])}
    }
    movies = []
    for title in MOVIE_RECOMMENDATIONS.get(career, []):
        movie_data = get_movie(title)
        movies.append({
        "Title": movie_data.get("Title"),
        "Year": movie_data.get("Year"),
        "Genre": movie_data.get("Genre"),
        "Plot": movie_data.get("Plot")
    })

    result["movies"] = movies


    dogimage_uri = "https://dog.ceo/api/breeds/image/random"
    respd = httpx.get(dogimage_uri).json()
    dog_url = respd['message']
    dog_file = "data/" + dog_url.split("/")[-1]

    with httpx.stream("GET", dog_url, follow_redirects=True) as response:
        response.raise_for_status()
        with open(dog_file, 'wb') as fout:
            for chunk in response.iter_bytes():
                fout.write(chunk)

    # duck uri
    duckimage_uri = "https://random-d.uk/api/v2/random"
    respd = httpx.get(duckimage_uri).json()
    duck_url = respd['url']
    duck_file = "data/" + duck_url.split("/")[-1]

    with httpx.stream("GET", duck_url, follow_redirects=True) as response:
        response.raise_for_status()
        with open(duck_file, 'wb') as fout:
            for chunk in response.iter_bytes():
                fout.write(chunk)

    catimage_uri = "https://api.thecatapi.com/v1/images/search"
    respd = httpx.get(catimage_uri).json()
    cat_url = respd[0]['url']
    cat_file = "data/" + cat_url.split("/")[-1]

    with httpx.stream("GET", cat_url, follow_redirects=True) as response:
        response.raise_for_status()
        with open(cat_file, 'wb') as fout:
            for chunk in response.iter_bytes():
                fout.write(chunk)

    with open("data/profile.json", "w") as f:
        json.dump(result, f, indent=4)

    return result


