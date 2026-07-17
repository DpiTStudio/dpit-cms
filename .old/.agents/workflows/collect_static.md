---
description: Collect static files for Django with WhiteNoise
---
1. Ensure you are in the project root directory (`l:/PYTHON/PROJECTS/dpit-cms/mysite`).
   ```
   cd l:/PYTHON/PROJECTS/dpit-cms/mysite
   ```
2. Activate the virtual environment if not already active.
   ```
   . venv/Scripts/activate   # Windows PowerShell
   ```
3. Run Django's collectstatic command to gather all static assets and generate the manifest.
   ```
   python manage.py collectstatic --noinput
   ```
   // turbo
4. Verify that the `staticfiles` directory now contains a `css/hero.css` file and a `staticfiles.json` manifest.
5. Restart the Django server (or gunicorn) to apply the changes.
   ```
   python manage.py runserver 0.0.0.0:8000
   ```
   // turbo
