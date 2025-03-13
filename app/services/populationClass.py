

class PopulationData:
    
    year_range
    
    def __init__(self, country_name: str, historical_population: list):
        self.country_name: str = country_name
        self.__historical_population: list = historical_population #private attribute


    def get_year_range(self):
        years = [year["year"] for year in self.__historical_population]

        # Get the range from the first and last year
        return f"From {max(years)} to {min(years)}"

    def __repr__(self):
        return f"For the PopulationData(country_name={self.country_name}, " \
               f"We have {len(self.__historical_population)} historical_population records " \
               f"from {self.get_year_range()}"

    def get_population_for_year(self, year: int):
        """Get the population for the given year, from both historical."""
        try:
            # Check in historical data
            for record in self.__historical_population:
                if record["year"] == year:
                    return record["population"]

            # If no data for the year
            raise ValueError(f"No population data available for year {year}")
        except ValueError as ve:
            # Handle specific value error
            raise ve
        except Exception as e:
            # Catch all other exceptions
            raise Exception(f"Error occurred while fetching population for year {year}: {str(e)}")
