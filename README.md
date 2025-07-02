# flask_practice

# Project structure

my_flask_app/
│
├── app/
│   ├── __init__.py
│   ├── models/ 
│   │   └── user.py
│   ├── persistence/
│   │   └── user_repo.py
│   ├── services/
│   │   └── user_service.py
│   ├── routes/
│   │   └── user_routes.py
│   ├── schemas/
│   │   └── user_schema.py
│   └── config.py
│
├── run.py
├── requirements.txt
└── .env

# Project brief
Goal:
Create a backend REST API to manage users, recipes, and reviews for each recipe.


# Flow of Flask
Route → Service → Persistence → Database

    Route:          RESTful api endpoints defining CRUD operations
    Service:        Contains functions for business logic used by API routes in routes/
    Persistence:    Database connection & config
    Models:         Defines data structures 


# Common Commands

**** VIRTUAL ENVIRONMENT ****
    Set-ExecutionPolicy Unrestricted -Scope Process
    venv\scripts\activate


