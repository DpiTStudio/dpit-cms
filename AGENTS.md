# DPIT-CMS AI Agent Guide

This repository is a Django CMS project inside the `mysite/` folder. Use `mysite/` as the primary codebase root for all Django operations.

## Key facts

- The main Django project lives under `mysite/`.
- Application code is organized as Django apps in `mysite/`: `accounts`, `main`, `news`, `portfolio`, `services`, `reviews`, `cart`, `favorites`, `tickets`, `knowledge_base`, `mail`, `logfiles`, and others.
- Global settings and initialization are in `mysite/mysite/`.
- Environment configuration is loaded from `mysite/.env` via `django-environ`.
- The project uses Django 5.x / Python 3.14 and Celery with Redis.
- The custom user model is `accounts.User` (`AUTH_USER_MODEL`).

## Run commands

From repository root, use `cd mysite` first or run `python mysite/manage.py`.

- Install dependencies: `pip install -r mysite/requirements.txt`
- Run migrations: `python mysite/manage.py migrate`
- Create superuser: `python mysite/manage.py createsuperuser`
- Start local server: `python mysite/manage.py runserver`
- Run tests: `python mysite/manage.py test`
- Start Celery worker: `celery -A mysite worker --loglevel=info`
- Start Celery beat: `celery -A mysite beat --loglevel=info`

## Important files

- `mysite/README.md` — main project overview
- `mysite/mysite/README.md` — Django core configuration guide
- `mysite/mysite/settings.py` — all global project settings
- `mysite/mysite/SETTINGS_DOCUMENTATION_RU.md` — detailed settings documentation
- `mysite/manage.py` — Django management entrypoint
- `mysite/mysite/celery.py` — Celery integration
- `mysite/mysite/backup_tasks.py` — backup task implementation

## Code conventions

- Keep Django app structure standard: `models.py`, `views.py`, `urls.py`, `admin.py`, `tests.py`, templates, and static assets are app-specific.
- Use the existing app-level `README.md` files for module-specific behavior and business logic.
- Preserve Russian comments in source files; they document important implementation details and business rules.
- Prefer making changes in the `mysite/` app folders rather than adding duplicate logic at the root.
- Media files are served from `mysite/media/`; static assets are stored in `mysite/static/` and `mysite/staticfiles/`.

## Special project behavior

- `main` contains shared utilities, SEO mixins, and file naming helpers.
- `favorites` uses Django GenericForeignKey for cross-model "favorite" relations.
- `logfiles` provides admin tools for server log management.
- `mail` includes IMAP/SMTP integration and mail testing utilities.
- `backups/` contains backup scripts and archived data.
- `mysite/mysite/backup_tasks.py` and Celery are used for scheduled backups.

## When you need more details

Check these docs before making large changes:

- `mysite/README.md`
- `mysite/mysite/README.md`
- `mysite/mysite/SETTINGS_DOCUMENTATION_RU.md`
- any `README.md` inside the app folder for that app

## Best advice for AI tasks

- Search first within `mysite/`.
- For Django issues, inspect `mysite/mysite/settings.py` and app `urls.py` files.
- Avoid editing database migration history unless the task explicitly requires schema changes.
- Keep production-sensitive paths and `.env` values abstract; do not hardcode secrets.
