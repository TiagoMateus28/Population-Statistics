# Population-Statistics
Population Statistics data processing pipeline code challenge



# Setting Up

## Overall Requirements

For these challenge, you need:
1. Python;
2. Text editor (Visual Studio Code is recommended);
3. Git.
4. Postman (optional)
5. Check the following site to generate a API key and Url: [API-Ninjas](https://api-ninjas.com/api/population)

## Clonning a repository

1. Open terminal (you can use the integrated terminal in visual studio);
2. Enter "git clone [Population-Statistics](https://github.com/TiagoMateus28/Population-Statistics.git)";
3. Ensure the project was correctly cloned.

# ENV Create / Install / Active

1. Create a new environment `python -m venv [NAME]`;
2. Activating the environment `./[NAME]/Scripts/activate`;
3. Installing a list of requirements `pip install -r [REQUIREMENTS_FILE_NAME].txt`.

Additional: creating a requirements file `pip -freeze > requirements.txt`.


# Set up environment variables

1. API_KEY=your_population_api_key_here
2. API_URL = https://api.api-ninjas.com/v1/population

# How to run locally

1. Ensure the virtual environment is active
2. Make sure you are at the app folder level
3. Use the following command "uvicorn main:app --reload" (Image

![image](https://github.com/user-attachments/assets/6e961218-54d5-4ac9-8b02-ca4f5886136d)

5. The FastAPI application will be accessible at e.g.`http://127.0.0.1:8000`.
6. Add the http://127.0.0.1:8000 + /docs to open the Interactive API Documentation

![image](https://github.com/user-attachments/assets/438af688-7e06-41b2-8d85-953a2e48bf14)

8. After the previous step test the endpoint by giving input as follows:

![image](https://github.com/user-attachments/assets/8c5ab5f9-145a-435e-8a83-a070c14dbcd0)


# API Documentation

### The API exposes one endpoint (for now):

GET /population/{country_name}

Request example: http://127.0.0.1:8000/population/Portugal?year=2023

Response example: 
{
  "country": "Portugal",
  "year": 2023,
  "population": 10430738
}

### Description

Fetches the current population size for a given country and year.

### Path Parameters

country_name (string) (required)
The name of the country for which the population data is being requested. Example: "USA", "India".

### Query Parameters

year (integer) (required)
The year for which the population data is requested. The value must be between 1995 and 2024, inclusive.
Example: 2000, 2010, 2020.

### Constraints
The year parameter must be a valid integer between 2024 and 1995.




