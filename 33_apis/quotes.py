import requests


api_key = "MrwAB+38ufv0mi2AP0Gz4w==ueHogxcgtaS75lW9"
category = 'happiness'

CATEGORY_LIST = [
   "age",
   "alone",
   "amazing",
   "anger",
   "architecture",
   "art",
   "attitude",
   "beauty",
   "best",
   "birthday",
   "business",
   "car",
   "change",
   "communication",
   "computers",
   "cool",
   "courage",
   "dad",
   "dating",
   "death",
   "design",
   "dreams",
   "education",
   "environmental",
   "equality",
   "experience",
   "failure",
   "faith",
   "family",
   "famous",
   "fear",
   "fitness",
   "food",
   "forgiveness",
   "freedom",
   "friendship",
   "funny",
   "future",
   "god",
   "good",
   "government",
   "graduation",
   "great",
   "happiness",
   "health",
   "history",
   "home",
   "hope",
   "humor",
   "imagination",
   "inspirational",
   "intelligence",
   "jealousy",
   "knowledge",
   "leadership",
   "learning",
   "legal",
   "life",
   "love",
   "marriage",
   "medical",
   "men",
   "mom",
   "money",
   "morning",
   "movies",
   "success"]


def get_quote(category="happiness"):
    api_url = f'https://api.api-ninjas.com/v1/quotes?category={category}'
    response = requests.get(api_url, headers={'X-Api-Key': f'{api_key}'})
    response.raise_for_status()
    if response.status_code == requests.codes.ok:
        text = response.json()
        print(f"{text[0]['quote']} - {text[0]['author']}")
    else:
        print("Error:", response.status_code, response.text)


get_quote()