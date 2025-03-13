


class PopulationData:
    def __init__(self, country_name: str, historical_population: list):
        self.country_name: str = country_name
        self.__historical_population: list = historical_population  # private attribute

    def get_year_range(self):
        years = [year["year"] for year in self.__historical_population]
        return f"From {min(years)} to {max(years)}"

    def __repr__(self):
        return f"For the PopulationData(country_name={self.country_name}, " \
               f"We have {len(self.__historical_population)} historical_population records " \
               f"from {self.get_year_range()}"

    def get_population_for_year(self, year: int):
        """Get the population for the given year, from historical data."""
        for record in self.__historical_population:
            if record["year"] == year:
                return record["population"]

        raise ValueError(f"No population data available for year {year}")
