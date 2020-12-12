# Python Web Servers Performance

```bash
docker-compose build
docker-compose build --no-cache

docker-compose up

docker-compose run database
docker-compose run web-server

docker exec -it postgre-database-container bash

git log --pretty=oneline
git push origin f61b48cb8b1877721e2596a6aa65648a68bb605e:master 
```

todo:

- [x] Setup a flask server in Docker using debug WSGI
- [x] Setup postgres in docker
- [x] Setup docker-compose
- [x] Setup postgre client in Flask in a naive way
- [x] fix fixed-data step in database
- [x] seed data in postgre
- [x] do something simple that involves reading from db and processing data
- [x] Setup loadimpact/k6 in Docker
- [x] Limit database and web-server cpu and memory in Docker
- [x] Print postgresql connections => pgAdmin
- [x] install k6 locally and test again to see if it performs better => yes but still not enough connections to db
- [x] Create an even worse way to use psycopg
- [x] Replicate load Error
psycopg2.OperationalError
psycopg2.OperationalError: FATAL:  remaining connection slots are reserved for non-replication superuser connections
- [ ] make k6 show a report of failed vs success
- [ ] calculate an approximation of the performance of the server

later:

- psycopg: For production use you are advised to use the source distribution. The binary packages come with their own versions of a few C libraries, among which libpq and libssl, which will be used regardless of other libraries available on the client: upgrading the system libraries will not upgrade the libraries used by psycopg2. Please build psycopg2 from source if you want to maintain binary upgradeability.

- alphine and psycopg2: https://www.rockyourcode.com/install-psycopg2-binary-with-docker/
https://pythonspeed.com/articles/base-image-python-docker-images/