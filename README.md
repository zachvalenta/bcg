## what (is this)?

A demo Flask API.

## how (to run locally)?

1) create a symlink `.env` to `.env.dev`

2) create and activate a virtual environment

3) `make install`

4) `make help`

```sh
/U/z/D/z/m/s/l/p/f/bcg $ make

🍶 FLASK

flask:       start app
home:        open homepage
get:         GET first seeded record

🛠  DB UTILS

seed:        seed db
shell:       open db REPL

📊 CODE QUALITY

test:        run unit tests
cov:         view coverage report

📦 DEPENDENCIES

freeze:      freeze dependencies into requirements.txt
install:     install dependencies from requirements.txt
purge:       remove any installed pkg *not* in requirements.txt
```

## design choices

* __SQLAlchemy and SQLite__: thought about TinyDB but I think I'm a relational person at heart
* __pytest__: still like xunit-style fixtures but more used to ecosystem around pytest these days
* __Serverless__: probably 1/3 of development time was just reading about Serverless (which has an interesting business model, makes me think of Render but that might be a facile comparison) but then I recalled my local npm install is broken so Serverless for another day
