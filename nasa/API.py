import requests

api_key = "G7QhgNjKjMCvbu0VzHUb7abZGGWpemBDZwlaesh1"
url= f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
response = requests.get(url)
