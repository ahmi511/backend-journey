import requests
from typing import Dict, Any

def get_pokemon_data(pokemon_name: str) -> None:
    print(f"Fetching data for {pokemon_name}...")
    
    # We are sending a GET request to a public API
    url: str = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        # The API returns JSON, which we immediately convert into a Python Dictionary!
        data: Dict[str, Any] = response.json()
        
        name = data["name"].capitalize()
        weight = data["weight"]
        
        print(f"Success! {name} weighs {weight} hectograms.")
    else:
        print(f"Failed to find {pokemon_name}. Status code: {response.status_code}")

# Let's test it out
get_pokemon_data("pikachu")