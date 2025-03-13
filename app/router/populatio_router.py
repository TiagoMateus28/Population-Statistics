# routers/population.py
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from services.popolation_services import PopulationService

# Create a router instance
router = APIRouter()

# Instantiate PopulationService
population_service = PopulationService()

@router.get("/population/{country_name}", description="Retrieve the population of a given country for a specified year.")
async def get_population(country_name: str, year: int = Query(..., ge=1995, le=2024)): # Query to ensure the year is within the range of 2024 to 1995
    try:
        # Get population for the year using the service
        population = population_service.get_population_for_year(country_name, year)
        return {"country": country_name, "year": year, "population": population}
    except HTTPException as e:
        raise e
    except ValueError:
        # Custom error message for invalid integer value
        raise HTTPException(status_code=422, detail="Year must be an integer.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
