# Celery
### Prerequisite
Must have Redis installed

### Run redis
```sh
redis-server
```

### Run celery
```sh
celery -A project_celery worker -l INFO
```

### Setup django:
* Clone repository
```sh
git clone https://github.com/ongraphpythondev/celery.git
```
* Create virtual environment
```sh
python3 -m venv myenv
```
* Activate virtual environment
```sh
source myenv/bin/activate
```
* Change directory
```sh
cd Celery
```
* Install all the dependencies:
```sh
pip install -r requirements.txt
```
* Run server:
```sh
python3 manage.py runserver
```