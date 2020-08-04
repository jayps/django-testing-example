# Django REST Framework Testing Example

## Getting started
- Create a virtual environment. Consider using pyenv for this, it's awesome.
- `pip install -r requirements.txt`

### Run the application
`python manage.py runserver`

### Run tests
`coverage run --source='.' manage.py test djangotesting`

### Get coverage (command line) 
`coverage report`

### Get coverage (HTML) 
`coverage html`