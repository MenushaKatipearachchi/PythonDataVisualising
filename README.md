# Django Project

This is a Django project that reads data from CSV files and populates a database.

## Getting Started

### Prerequisites

- Docker
- Python 3.8
- Django

### Installing and Running

1. Build the Docker image: `docker build -t django-image .`
2. Create a Docker volume: `docker volume create django_db_volume`
3. Run the Docker image: `docker run -d -p 8000:8000 -v django_db_volume:/var/lib/postgresql/data --name my_django_container django-image`
4. Execute makemigrations command: `docker exec my_django_container python manage.py makemigrations`
5. Execute migrate command: `docker exec my_django_container python manage.py migrate`
6. Execute the populate DB command: `docker exec my_django_container python manage.py populate_db_command`
7. In your browser type `http://localhost:8000/` to see the visualization

## Running the tests

To run the automated tests for this system. Make sure your Docker container is running by checking `### Installing and Running` and run this command in terminal: `docker exec my_django_container python manage.py test hello/test`

## Built With

- Django - The web framework used
- Docker - Used for containerization

## Authors

- **Menusha Katipearachchi** - _Initial work_ - `https://github.com/MenushaKatipearachchi`

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments
