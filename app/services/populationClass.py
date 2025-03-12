

class PopulationData:
    def __init__(self, country_name: str, historical_population: list, population_forecast: list):
        self.country_name = country_name
        self.historical_population = historical_population
        self.population_forecast = population_forecast

    def __repr__(self):
        return f"PopulationData(country_name={self.country_name}, " \
               f"historical_population={len(self.historical_population)} records, " \
               f"population_forecast={len(self.population_forecast)} records)"

    def get_population_for_year(self, year: int):
        """Get the population for the given year, from both historical and forecasted data."""
        try:
            # Check in historical data
            for record in self.historical_population:
                if record["year"] == year:
                    return record["population"]

            # Check in forecasted data
            for forecast in self.population_forecast:
                if forecast["year"] == year:
                    return forecast["population"]

            # If no data for the year
            raise ValueError(f"No population data available for year {year}")
        except ValueError as ve:
            # Handle specific value error
            raise ve
        except Exception as e:
            # Catch all other exceptions
            raise Exception(f"Error occurred while fetching population for year {year}: {str(e)}")
