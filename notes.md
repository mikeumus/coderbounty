### Notes

- ERROR: `django AttributeError: 'NoneType' object has no attribute 'tags'`
 - Please use `django-material==0.5.1` in `requirements.txt`
 - See: https://github.com/viewflow/django-material/issues/51#issuecomment-159009453

- NOTE: Install `requirements.txt`
 - Simply run: `pip install -r requirements.txt` on the same directory that you see `requirements.txt` which for CoderBounty at the time of this writing is the root of the project. 
 
- ERROR: `Exception Value: Unknown parameters: TEMPLATE_DEBUG`
 - Django 1.8 and above doesn't use `TEMPLATE_DEBUG` in `settings.py`
 - Instead use: 
    ```
    TEMPLATES = [
        {
            # something else
            'OPTIONS': {
                'debug': DEBUG,
            },
        },
    ]
    ```
 - From https://stackoverflow.com/questions/34298867/django-settings-unknown-parameters-template-debug