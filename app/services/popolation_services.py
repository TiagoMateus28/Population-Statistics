
import requests

from populationClass import *

from app.config import Config  # Import the Config class


# global variables

headers = Config.headers


def get_country_population(country : str) -> PopulationData:
    """Fetch the current population for a given country from the API Ninjas API."""
    
    try:
        
        params = {"country": country}
        
        #GET request
        response = requests.get(Config.API_URL, headers=headers, params=params)

        # Check if the response is successful
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the response JSON
        data = response.json()

        # Check for errors in the response data
        if "error" in data:
            raise ValueError(f"Error from API: {data['error']}")

        # Extract historical population data
        historical_population = data.get("historical_population")
        if not historical_population:
            raise ValueError(f"Historical population data not found for {country}")

        # Return a PopulationData instance containing the data
        return PopulationData(country_name=country, historical_population=historical_population)

    except requests.exceptions.RequestException as e:
        # Handle network-related errors or invalid requests
        raise Exception(f"Request error: {e}")

    except ValueError as e:
        # Handle errors related to invalid data or missing data
        raise Exception(f"Data error: {e}")

    except Exception as e:
        # Handle any other unforeseen errors
        raise Exception(f"An unexpected error occurred: {e}")
