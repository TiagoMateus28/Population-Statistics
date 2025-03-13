import requests
from class_definition.populationClass import PopulationData
from fastapi import HTTPException
from config import Config

class PopulationService:
    def __init__(self):
        self.api_url = Config.api_url  # External API URL
        self.api_key = Config.api_key  # API Key for authentication

    def fetch_population_data(self, country_name: str):
        """Fetch population data from an external API based on the country name."""
        
        # Assuming the external API requires country as a query parameter
        url = f"{self.api_url}?country={country_name}"
        headers = Config.headers  # Headers containing the API key
        print(url)
        print(headers)
        try:
            # Sending GET request to the external API
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an exception for 4xx or 5xx responses

            data = response.json()

            # Check if the expected key is present in the response
            if "historical_population" not in data:
                raise HTTPException(status_code=404, detail="Historical population data not found.")
            
            return data["historical_population"]  # Return the historical population data

        except requests.exceptions.RequestException as e:
            # Handle any request-related errors (timeouts, network issues, etc.)
            raise HTTPException(status_code=500, detail=f"API request failed: {str(e)}")
        except ValueError:
            # Handle errors when parsing JSON response
            raise HTTPException(status_code=500, detail="Failed to parse API response as JSON.")
        
    def get_population_for_year(self, country_name: str, year: int):
        """Fetch population for a given country and year."""
        # Fetch the historical population data for the given country
        try:
            # Fetch the historical population data
            historical_population = self.fetch_population_data(country_name)
            
            # Create an instance of PopulationData to handle the historical population data
            population_data = PopulationData(country_name, historical_population)
            
            # Get the population for the specified year
            return population_data.get_population_for_year(year)

        except HTTPException as e:
            # Re-raise any HTTPException raised during the process
            raise e
        except Exception as e:
            # Catch any unexpected errors and raise a generic HTTPException
            raise HTTPException(status_code=500, detail=f"Error fetching population data: {str(e)}")
