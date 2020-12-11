# Python Web Servers Performance

```bash
docker-compose build
docker-compose build --no-cache

docker-compose up

docker exec -it postgre-database-container bash

psql -h localhost -p 5432 -U test_user test_database
```

todo:

- [x] Setup a flask server in Docker using debug WSGI
- [x] Setup postgres in docker
- [x] Setup docker-compose
- [x] Setup postgre client in Flask in a naive way
- [ ] fix fixed-data step in database
- [ ] seed data in postgre
- [ ] do something that involves reading from db and processing data
- [ ] Setup loadimpact/k6 in Docker
- [ ] Load balance the flask debug server
- [ ] make something fail by excess load
- [ ] make something more complex https://linuxconfig.org/random-word-generator

later:

- psycopg: For production use you are advised to use the source distribution. The binary packages come with their own versions of a few C libraries, among which libpq and libssl, which will be used regardless of other libraries available on the client: upgrading the system libraries will not upgrade the libraries used by psycopg2. Please build psycopg2 from source if you want to maintain binary upgradeability.

- alphine and psycopg2: https://www.rockyourcode.com/install-psycopg2-binary-with-docker/
https://pythonspeed.com/articles/base-image-python-docker-images/