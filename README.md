## Mood Badger

Mood reporting API service run using Django


### Environment Variables

```
DJANGO_SECRET_KEY=...
DJANGO_DEBUG=...
DJANGO_HOST=...
```

### Build and Run with Docker Compose

```
docker-compose up --build -d
```
Accessed on `localhost:8000`

The sqlite database file in the repo at `moodbadger/db.sqlite3` includes test admin and test users.
* Admin `syd`
* Users testuser1, testuser2, testuser3, testuser4
* All have password `abc123!!!`

If the database is not included in the docker build, a new sqlite database will be created and migrations automatically applied.

### Endpoints

**POST /rest-auth/login/** - Log in

Takes body arguments `username` and `password`
e.g. `{"username": "testuser1", "password": "abc123"}`

**POST /rest-auth/logout/** - Log out

**POST /mood** - Create a mood report

Takes body argument `description`
e.g. `{"description": "Good mood"}`

**GET /mood** - Get historical mood reports for logged in user including longest reporting streak and streak percentile compared to other users


### Potential Improvements for Production

* Timezone consideration for streak so it's based on user's timezone rather than the server's timezone
* Avoid doing a full table scan every request for streak percentile by precalculating periodically per user
* Use a remote database
* Better security practices:
  * Secure secret key
  * Limit allowed hosts in Django and Docker
  * Don't server static files with the staticfiles app
    