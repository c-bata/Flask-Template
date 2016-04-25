# Awesome flask libraries

## About

This is flask awesome libraries and example application.


## Libraries

#### Databases

- [SQLAlchemy](http://www.sqlalchemy.org/) / [Flask-SQLAlchemy](https://github.com/mitsuhiko/flask-sqlalchemy)
- [Alembic](https://bitbucket.org/zzzeek/alembic) / [Flask-Migrate](https://github.com/miguelgrinberg/Flask-Migrate)
- [PyMySQL](https://github.com/PyMySQL/PyMySQL) / [psycopg2](https://github.com/psycopg/psycopg2)
- [redis](https://github.com/andymccurdy/redis-py)
- [pymongo](http://github.com/mongodb/mongo-python-driver)

- [Flask-Admin](https://github.com/mrjoes/flask-admin/)


#### Authentication

- [Werkzeug](https://github.com/mitsuhiko/werkzeug)

```
>>> from werkzeug.security import generate_password_hash, check_password_hash
>>> password_hash = generate_password_hash('my password')
>>> check_password_hash(password_hash, 'my password')
True
>>> check_password_hash(password_hash, 'this is not my password')
False
```

- [PyJWT](https://github.com/jpadilla/pyjwt)

```
>>> import jwt
>>> from datetime import datetime, timedelta
>>> payload = {
...     'user_id': 1,
...     'iat': datetime.utcnow(),
...     'exp': datetime.utcnow() + timedelta(days=1)
... }
>>> token = jwt.encode(payload, 'SECRET_KEY')
>>> token
b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE0NDY4NzczNjIsImlhdCI6MTQ0Njc5MDk2Mn0.JVjdlg_0lxDtl4AqHRpiC4Gpv1hkB57g5dsIyWJmnF4'
>>> token.decode('unicode_escape')
'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE0NDY4NzczNjIsImlhdCI6MTQ0Njc5MDk2Mn0.JVjdlg_0lxDtl4AqHRpiC4Gpv1hkB57g5dsIyWJmnF4'

>>> jwt.decode(token, 'SECRET_KEY')
{'user_id': 1, 'exp': 1446877362, 'iat': 1446790962}
>>> jwt.decode(token, verify=False)
{'user_id': 1, 'exp': 1446877362, 'iat': 1446790962}
```

- [itsdangerous](https://github.com/mitsuhiko/itsdangerous)

```
>>> from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

>>> s = Serializer('SECRET_KEY', expires_in=3600)
>>> token = s.dumps({'id': 1}).decode('utf-8')
>>> token
'eyJleHAiOjE0NDY3OTYwMTQsImFsZyI6IkhTMjU2IiwiaWF0IjoxNDQ2NzkyNDE0fQ.eyJpZCI6MX0.2d2h08XCqbMOgZw918jFRf2lJH_9QQwrQrJp5CnpbSI'

>>> s = Serializer('SECRET_KEY')
>>> s.loads(token)
{'id': 1}
>>> s.loads('dummy.token')
Traceback (most recent call last):
  :
  :
itsdangerous.BadSignature: Signature b'token' does not match
```



#### Utils

- [Flask-Script](https://github.com/smurfix/flask-script)
- [salchemyjsonschema](https://github.com/podhmo/alchemyjsonschema)
- [Flask Debug-toolbar](https://github.com/mgood/flask-debugtoolbar)
- [flask-profiler](https://github.com/muatik/flask-profiler)


#### Profiling

- [Flask-SQLAlchemy](https://github.com/mitsuhiko/flask-sqlalchemy)

```
# api/__init__.py
@app.after_request
def after_request(response):
    for query in get_debug_queries():
        if query.duration >= app.config['SLOW_DB_QUERY_TIME']:
            app.logger.warning(
                'Slow query: %s\nParameters: %s\n'
                'Duration: %fs\nContext: %s\n'
                % (query.statement, query.parameters,
                   query.duration, query.context)
            )
    return response
```


- [Werkzeug](https://github.com/mitsuhiko/werkzeug)

```
# manage.py
@manager.command
def profile(length=25):
    """Start the application under the code profiler."""
    from werkzeug.contrib.profiler import ProfilerMiddleware
    app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[length])
    app.run()
````



## License

This software is licensed under the MIT License.

