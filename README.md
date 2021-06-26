# Setup
## With Docker
For running on Docker in Dev mode just run following command in terminal:

```sh
docker-compose up
```

For running on Docker in Production mode just run following command in terminal:

```sh
$ docker-compose -f docker-compose.prod.yml up -d --build
$ docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
$ docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
```
## Without Docker
For running without Docker in Dev mode:
* Uncomment the following lines in settings.py:
```sh
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv(".env.dev"))
```
* change SQL_HOST in .env.dev to `localhost`
* active your virtual environment and run following command in terminal:

```sh
cd app
source .venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

*Note: Keep the env files secure.*