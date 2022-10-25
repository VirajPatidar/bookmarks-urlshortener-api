# Bookmarks + URL Shortener API

_An [API](https://bookmarks-urlshortner-api.herokuapp.com) to create and manage bookmarks with a URL shortening service <br/>_


**Link to the API docs:** [https://bookmarks-urlshortener-api.up.railway.app/](https://bookmarks-urlshortener-api.up.railway.app/) <br/>


### Tech Stack ###
  * Flask
  * Semantic UI
  * Flask-JWT-Extended
  * Flask-SQLAlchemy
  * Flasgger
  * Jinja2
  * SQLite

<br/>

### API Endpoints ###
**Authentication**
| Method | API Endpoint | Description |
| :---         | :---         | :---
| `POST`     | `/auth/register`       |  To register new user      |
| `POST`   | `/auth/login`     | To login using email - password    |
| `GET`   | `/auth/token/refresh`     | To refresh the token (get new access token)    |
| `GET`     | `/auth/me`       |  To get user profile data      |

<br/>

**Bookmarks + URL Shortener**
| Method | API Endpoint | Description |
| :---         | :---         | :---
| `POST`     | `/bookmarks`       |  To create a new bookmark      |
| `GET`   | `/bookmarks`     | To get bookmarks collection (Use query params for pagination Example: /bookmarks/?page=2)    |
| `GET`   | `/bookmarks/stats`     | To get statistics of all bookmarks    |
| `GET`   | `/bookmarks/{id}`     | To get bookmark by id    |
| `DELETE`   | `/bookmarks/{id}`     | To delete bookmark by id    |
| `PUT`   | `/bookmarks/{id}`     | To update bookmark by id    |
| `PATCH`   | `/bookmarks/{id}`     | To update bookmark by id    |
| `GET`     | `/{short_url}`       |  Redirects to original URL using short_url  |

<br/>


### Setup ###
Create project with virtual environment

```console
$ mkdir myproject
$ cd myproject
$ python3 -m venv venv
```

Activate it
```console
$ . venv/bin/activate
```

or on Windows
```console
venv\Scripts\activate
```

Install Dependencies
```console
$ pip install -r requirements.txt
```

Set environment variables in terminal
```console
$ export FLASK_APP=src
$ export FLASK_ENV=development
$ export SQLALCHEMY_DB_URI=sqlite:///bookmarks.db
$ export SECRET_KEY="your secret key"
$ export JWT_SECRET_KEY="your JWT secret key"
```

or on Windows
```console
$ set FLASK_APP=src
$ set FLASK_ENV=development
$ set SQLALCHEMY_DB_URI=sqlite:///bookmarks.db
$ set SECRET_KEY="your secret key"
$ set JWT_SECRET_KEY="your JWT secret key"
```

Run the app
```console
$ flask run
```
