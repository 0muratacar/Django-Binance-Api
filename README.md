
# Introduction

The Django Binance App is a web application designed to retrieve account balance information from the Binance API and store it in a PostgreSQL database. It leverages Docker for containerized deployment, Celery for asynchronous task processing, Redis for task management, and serializers for data serialization.

# Installation
To run the Django Binance App, follow these steps:

- Clone the repository.
```bash
git clone https://github.com/0muratacar/Django-Binance-Api.git
````

- Create a .env file in the root directory of your project and add the following environment variables. Replace the placeholders with your actual values.
```bash
BINANCE_API_KEY = 'XXX'
BINANCE_SECRET_KEY = 'XXX'
```

- Execute this command to run shell commands in docker-compose file 

```bash 
chmod +x entrypoint.sh
```

- Make sure that Docker is installed and running on your system

```bash
docker --version
```

- Build and Start Containers

```bash
docker-compose up --build
```
<hr>

## Now you can access the application.
<hr>

- To stop and remove the Docker containers, use the following command:

```bash
docker-compose down
docker system prune --all
```



# API Documentation
This documentation provides an overview of the API endpoints and functionality offered by the Django Binance App.

Base URL
The base URL for the API endpoints is: http://localhost:8000/ (or your server's URL).

Authentication
No authentication is required to access these endpoints.

# Endpoints

The base URL for the API endpoints is: http://localhost:8000/ (or your server's URL).



1. Get Binance Initialization Status

    URL: /

    Method: GET

    Response:
    
     {"message": "Binance initialized successfully!"}
    
    OR

     {"message": "Check Binance Client!"}

    Description: Check the status of Binance client initialization.

<hr>

2. Get Binance Account Details

    URL: /account

    Method: GET

    Description: Retrieve account details from the Binance API.

<hr>


3. Get Non-Zero Balances from Binance Account

    URL: /balances-api

    Method: GET

    Description: Retrieve non-zero balances from the Binance account.

<hr>


4. Get All Balances from Database

    URL: /balances-db

    Method: GET

    Description: Retrieve all balances from the database.

5. Get Balance by ID

    URL: /balances-db/<int:id>

    Method: GET 

    Description: Retrieve a specific balance by ID from the database. 

<hr>


6. Create Balance

    URL: /balances-db

    Method: POST

    Fields

    - name: CharField (max_length=100)

        Description: The name associated with the balance.
        Maximum Length: 100 characters

    - balance: FloatField
        Description: The balance amount.
        Type: Float

    Description: Retrieve all balances from the database.