# Bookmarks + URL Shortener API

_An [API](https://bookmarks-urlshortner-api.herokuapp.com) to create and manage bookmarks with a URL shortening service <br/>_


**Link to the API docs:** [https://bookmarks-urlshortner-api.herokuapp.com](https://bookmarks-urlshortner-api.herokuapp.com) <br/>

<br/>


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

**Authentication**
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
