# Load Testing

```sh
docker build -t load-test .

docker run --network=host load-test

docker run --network=host load-test run --vus 1000 --iterations 1000 script.js

```