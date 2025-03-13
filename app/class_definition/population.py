

from population import PopulationData
from fastapi import HTTPException

class PopulationService:
    def __init__(self, population_data: dict):
        self.__population_data = population_data

    def get_population_for_year(self, country_name: str, year: int):
        """Fetch population for a given country and year."""
        country_data = self.__population_data.get(country_name)

        if not country_data:
            raise HTTPException(status_code=404, detail="Country not found")

        population_data = PopulationData(country_name, country_data["historical_population"])
        return population_data.get_population_for_year(year)
