# Portfolio Website

A personal portfolio website built with Wagtail CMS, styled with Tailwind CSS, and powered by PostgreSQL.

## Technologies

- Python 3.11+
- Wagtail 7.0
- Tailwind CSS
- PostgreSQL
- Poetry for dependency management

## Prerequisites

- Python 3.11 or higher
- PostgreSQL
- Poetry package manager

## Local Development Setup

1. Clone the repository:
```bash
git clone <your-repository-url>
cd portfolio
```

2. Install dependencies using Poetry:
```bash
poetry install
```

3. Create a `.env` file in the project root:
```plaintext
POSTGRES_HOST=<something>
POSTGRES_PORT=<something>
POSTGRES_USER=<something>
POSTGRES_PASSWORD=<something>
DEBUG=True
SECRET_KEY=<something>
ALLOWED_HOSTS=<something>
```

4. Initialize the database:
```bash
poetry run python manage.py migrate
poetry run python manage.py createsuperuser
```

5. Start the development server:
```bash
poetry run python manage.py runserver
```

6. Visit http://127.0.0.1:8080 in your browser

## Features

- Responsive design with Tailwind CSS
- Blog functionality
- Project showcase
- Contact form
- SEO optimized pages
- Mobile-friendly navigation

## Deployment

The project is configured to run in a Docker container. Build and run using:

```bash
docker-compose up --build
```

## License

[Your chosen license]

## Author

Andreas Cormack
