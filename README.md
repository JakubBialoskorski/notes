# Notty

Flask notes app with MySQL as a backend.

Heavily based on [this repository](https://github.com/OmkarPathak/A-Simple-Note-Taking-Web-App) but with MySQL / Aurora support (instead of local SQLite)

`strftime` was cut out along with any time-related functions.

### How to develop:
* `pip install -r requirements.txt`
* set your MySQL credentials in `utils/functions.py`
* run initial schema from `schema_mysql.sql`
* `python manage.py`