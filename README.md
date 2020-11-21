# Notty

Flask notes app with MySQL as a backend.
---
Based on [this repository](https://github.com/OmkarPathak/A-Simple-Note-Taking-Web-App) but with:
* MySQL / Aurora support (instead of local SQLite)
* `strftime` was cut out along with any time-related functions
* all `delete` actions explicit confirmations
* dockerized app and unit tests, easily deployable via CI/CD
* support for `utfmb4` (special characters like `śćźżó` / emojis etc.)
* bumped dependencies to match Snyk scans recommendations
---
#### How to develop:
* `pip install -r requirements.txt`
* create a database with `utf8mb4` charset and `utf8mb4_unicode_ci` collation
* set your MySQL credentials in `utils/functions.py`
* run initial schema from `schema_mysql.sql`
* `python manage.py` or `gunicorn manage:app`
---
#### How to run locally in Docker:
* `docker build . -t notty-development`
* `docker run -d -p 80:80 -e SQLALCHEMY_CONFIG='mysql://USER:PASSWORD@DATABASE_IP/DATABASE_NAME' notty-development`

`SQLALCHEMY_CONFIG` can be put into Jenkins as build parameter to pass database credentials (though there are more secure methods).

You can also use bash helpers to speed-up development:
* Fill credentials in `build_and_run.sh` and run it to build the Dockerfile with `notty` as container name
* `stop_and_destroy.sh` quickly does the obvious and you can proceed with another change 