# Django REST Framework Testing Example

This repo contains a super basic DRF app with some super basic tests.

## Getting started
- Create a virtual environment. Consider using pyenv for this, it's awesome.
- `pip install -r requirements.txt`

### Run the application
`python manage.py runserver`

### Run tests
`coverage run --source='djangotesting.api' manage.py test djangotesting`

### Get coverage (command line) 
`coverage report`

### Get coverage (HTML) 
`coverage html`