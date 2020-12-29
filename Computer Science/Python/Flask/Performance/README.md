# Flask Postgre Performance

How to create slow and fast APIs

The worst way to create a Flask <-> psycopg app

```bash
docker-compose build
docker-compose build --no-cache

docker-compose up

docker-compose run database
docker-compose run web-server

docker exec -it postgre-database-container bash

git log --pretty=oneline
git push origin f61b48cb8b1877721e2596a6aa65648a68bb605e:master 

docker build --tag web-server-image ./Good\ Flask\ Postgres

docker run -it -p 3000:3000 --name web-server-container -v "$(pwd)/Good\ Flask\ Postgres:/usr/src/app" --cpus 0.20 --memory 200M --network flask-perf-net web-server-image


docker-compose  -f Good\ Flask\ Postgres/docker-compose.yml build web-server

docker-compose -f Good\ Flask\ Postgres/docker-compose.yml run web-server

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
- [x] learn iterators
- [x] learn with and context managers
- [x] learn threads in python
- [x] implement threadedpool in pyscopg with Flask
- [x] perf test the good flask with treadedpool => awesome perf
- [x] make k6 show the rate of failed requests
- [x] use psycopg cursor_factory=psycopg2.extras.RealDictCursor
- [x] return payload in JSON
- [x] add response checks to load-test
- [ ] handle psycopg2.pool.PoolError: connection pool exhausted Errors
return self._getconn(key)
- [ ] add connection pool exhausted checks to load-test
raise PoolError("connection pool exhausted")
- [ ] calculate an approximation of the performance of the server

later:

Pool doesn't keep connections open #563
https://github.com/psycopg/psycopg2/issues/563
https://www.psycopg.org/docs/pool.html

- psycopg: For production use you are advised to use the source distribution. The binary packages come with their own versions of a few C libraries, among which libpq and libssl, which will be used regardless of other libraries available on the client: upgrading the system libraries will not upgrade the libraries used by psycopg2. Please build psycopg2 from source if you want to maintain binary upgradeability.

- alphine and psycopg2: https://www.rockyourcode.com/install-psycopg2-binary-with-docker/
https://pythonspeed.com/articles/base-image-python-docker-images/


## Links

[Python PostgreSQL Connection Pooling Using Psycopg2](https://pynative.com/psycopg2-python-postgresql-connection-pooling/#psycopg2s_AbstractConnectionPool)

## Links to read

https://www.programcreek.com/python/example/117833/psycopg2.pool.ThreadedConnectionPool

https://medium.com/@thegavrikstory/manage-raw-database-connection-pool-in-flask-b11e50cbad3

https://paullockaby.com/archive/2019/09/flask-connection-pool-for-postgresql/
https://gist.github.com/plockaby/6fcdf51148f8b7035b8f451ebe583a82

https://medium.com/analytics-vidhya/setting-up-django-with-nginx-gunicorn-and-aws-ecs-e1b279c7ae8

This uses uwshi + Flask + pyscopg ThreadedConnectionPool
https://github.com/Oslandia/lopocs/tree/master/lopocs

https://www.damyanon.net/post/flask-series-optimizations/

https://pythonise.com/series/learning-flask/flask-configuration-files

https://arstechnica.com/information-technology/2015/10/patreon-was-warned-of-serious-website-flaw-5-days-before-it-was-hacked/

https://arusahni.net/blog/2013/10/flask-multithreading.html

https://dev.to/kokospapa8/gunicorn-performance-analysis-on-aws-ec2-28jl
https://blog.kgriffs.com/2012/12/18/uwsgi-vs-gunicorn-vs-node-benchmarks.html

fhttps://www.damyanon.net/post/flask-series-optimizations/