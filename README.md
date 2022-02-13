# Robot

## Getting up and running
This app requires [Python 3.7](https://www.python.org/downloads/) or greater.

Run the following commands to get up and running:
```
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
./manage.py runserver
coverage run --source='.' manage.py test myapp
```

Your app should be running at http://localhost:8000