# flask_practice

# Project structure

my_flask_app/
│
├── app/
│   ├── __init__.py
# contains table structure of each entity
│   ├── models/ 
│   │   └── user.py
# abstraction of common methods used frequently
│   ├── persistence/
│   │   └── user_repo.py
# contains functions for business logic used by files in routes/
│   ├── services/
│   │   └── user_service.py
# RESTful api endpoints defining CRUD operations
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
