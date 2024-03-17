import json
import os
import requests
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())  # This is to load your API keys from .env

# Update to fetch weekly trending TV shows
TMDB_TRENDING_PATH = 'trending/tv/week'
TMDB_SEARCH_API_REQUEST = f'https://api.themoviedb.org/3/{TMDB_TRENDING_PATH}?'

# def get_top_10_weekly_trending_tv_shows():
response = requests.get(
    TMDB_SEARCH_API_REQUEST,
    params={
        'api_key': os.getenv('TMDB_API_KEY')
    }
)
# Encodes response into a python json dictionary.
json_data = response.json()
print(json_data)

# Convert json_data to a formatted pretty
# json string that is easy for humans to read.
# Mouse over function to get definition of indent and sort_keys
pretty_json_data = json.dumps(json_data, indent=4, sort_keys=True)
print(pretty_json_data)

weekly_trending_tv_show_object = json_data


def print_data(data):
    # Limit to the top 10 results
    results = data.get('results', [])[:10]
    for item in results:
        print(
            f"Title: {item.get('name', '')}, Popularity: {item.get('popularity', '')}, Vote Count: {item.get('vote_count', '')}, Vote Average: {item.get('vote_average', '')}"
        )


def print_sorted_data(data):
    sorted_data = sorted(data.get('results', []),
                         key=lambda x: x.get('vote_average', 0), reverse=True)[:10]  # Limit to top 10 sorted results
    for item in sorted_data:
        print(
            f"Title: {item.get('name', '')}, Vote Average: {item.get('vote_average')}"
        )


print("\nData with Details:")
print_data(weekly_trending_tv_show_object)

# sorted data by vote average
print("\nSorted Data by Vote Average:")
print_sorted_data(weekly_trending_tv_show_object)
