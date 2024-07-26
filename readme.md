
# Django Application with API and Web3 Integration

## Overview

This Django application is designed to store data in a SQLite database and expose a RESTful API to interact with that data. The API supports filtering, sorting, and pagination and is secured with JWT authentication. Users can only interact with their own records.

## Features

1. **Data Storage**: Uses SQLite by default for simplicity.
2. **API**: Returns data with support for filtering, sorting, and pagination.
3. **Authentication**: Uses JWT authentication to ensure that only authenticated users can access the API.
4. **CRUD Operations**: Users can create, read, update, and delete their own records.
5. **Web3 Integration** (Optional): Tracks on-chain events from Web3 sources and stores the data.


I have successfully created the task in less than 40 minutes with minimal test cases. I haven't implemented Web3 Integration as I dont have any experience yet working with web 3

1. I've stored data in sqlite (if we were to use different database such as postgresql, I will just have to configure it in our settings.py and include the database url from an environment variable.)

2. Implemented an API that returns a data, it supports filtering, sorting, and pagination.
    - The API is also context aware, meaning that it only returns the records of those authenticated users.
    - I've implemented JWT authentication and required the APIs to have a user authenticated before interacting with it.

3. The API supports CRUD (Create, Read, Update, Delete) operations and users can only update their own records because it only shows their records.

4. For web3 and tracking on-chain events **(If I were to implement it)**
    - If the data source have like a webhook support, I would create a webhook receiver and would map events received to the user from the source and store it in database.
## Setup Instructions

### Prerequisites

- Python 3.x
- Django
- Django REST framework
- Django REST framework JWT

### Installation

1. **Clone the repository**:

   \`\`\`sh
   git clone <repository-url>
   cd <repository-directory>
   \`\`\`

2. **Create and activate a virtual environment**:

   \`\`\`sh
   python -m venv env
   source env/bin/activate   # On Windows use `env\Scripts\Activate`
   \`\`\`

3. **Install the required packages**:

   \`\`\`sh
   pip install -r requirements.txt
   \`\`\`

4. **Run database migrations**:

   \`\`\`sh
   python manage.py migrate
   \`\`\`

5. **Create a superuser**:

   \`\`\`sh
   python manage.py createsuperuser
   \`\`\`

6. **Run the development server**:

   \`\`\`sh
   python manage.py runserver
   \`\`\`

### Configuration

To use a different database (e.g., PostgreSQL), update the `DATABASES` setting in `settings.py`:

\`\`\`python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}
\`\`\`

## API Usage

### Endpoints

- **List Records**: `GET /api/records/`
  - Supports filtering, sorting, and pagination.
- **Retrieve Record**: `GET /api/records/<id>/`
- **Create Record**: `POST /api/records/`
- **Update Record**: `PUT /api/records/<id>/`
- **Delete Record**: `DELETE /api/records/<id>/`

### Authentication

Obtain a JWT token by sending a `POST` request to `/api/token/` with the user's credentials. Include the token in the `Authorization` header for all API requests:

\`\`\`http
Authorization: Bearer {your-token}
\`\`\`

### Example Request

\`\`\`sh
curl -X GET http://localhost:8000/api/records/ -H "Authorization: Bearer <your-token>"
\`\`\`

## Testing

Run the following command to execute the test cases:

\`\`\`sh
python manage.py test
\`\`\`

## Conclusion

This application provides a simple and secure way to interact with stored data via a RESTful API. The optional Web3 integration allows for tracking on-chain events and storing them in the database. The implementation is straightforward and easy to understand, making it accessible even for those without in-depth Django knowledge.
