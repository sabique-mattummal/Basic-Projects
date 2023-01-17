import requests
from question_model import Question

URL = "https://opentdb.com/api.php?amount=10&category=17&difficulty=medium&type=boolean"
data = requests.get(URL).json()['results']
