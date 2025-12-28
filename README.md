# eco-tomchi

A Django-based environmental news site inspired by magazine layouts (NewScientist-like). The project supports a block-based article editor (image + rich text blocks), a magazine-style homepage (hero + card grid), and an admin editor with live preview and typography/color presets.

---

## Features

- Block-based article editor (image & text blocks with per-block styling)
- Rich text editing with CKEditor
- Sortable inlines in the admin for ordering blocks
- Magazine-style homepage and article detail layouts
- Simple image management and featured images

## Tech stack

- Python 3.11+ / 3.14 (project tests on local environment)
- Django 6.x
- django-ckeditor
- django-admin-sortable2
- Whitenoise for static files

## Quick setup (development)

1. Create and activate a virtual environment:

   python -m venv .venv
   .venv\Scripts\activate

2. Install dependencies:

   python -m pip install -r requirements.txt

3. Configure environment variables (recommended):

   - Set `DJANGO_SECRET_KEY` and optionally `DATABASE_URL`.

4. Run migrations and start the server:

   python manage.py migrate
   python manage.py createsuperuser  # create admin user
   python manage.py runserver

5. Open the site in your browser:

   http://127.0.0.1:8000/  (site)
   http://127.0.0.1:8000/admin/  (admin)

## Admin editor notes

- The `Article` admin includes an inline `ArticleBlock` model. Each block can be an `image` or `text` block; text blocks use CKEditor for rich content.
- Use the palette and font presets in the admin block inline to quickly style text color, font family, and size. Live preview is available in the inline when editing.

## Development notes

- Static assets are collected to `staticfiles/` (run `python manage.py collectstatic`).
- Migrations are kept in `articles/migrations/` (e.g. added `0003_articleblock.py` for block support).
- Tests: run `python manage.py test`.

## Contributing

- Fork and submit PRs for feature additions or fixes. Please include tests and update docs when changing behavior.

---

If you'd like I can add a demo article and screenshots to show the updated detail page layout and admin editor. Send a message and I'll create them and commit the sample content.