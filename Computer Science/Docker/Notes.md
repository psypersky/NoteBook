

Problems with the example 3:
- If you have node_modules on the host machine it will be sent to the docker machine with the volume
- If you install a module how do you install it too in the machine?

Some usefull shit:
http://jdlm.info/articles/2016/03/06/lessons-building-node-app-docker.html

- Use unprivileged user (least privilege principle)
- use exact versions in Docker file, accidental upgrades
- Chain commands in RUN reduce the number of layer in the resulting image (effiency in space and time)
- Use npm shrinkwap to lock npm packages versions


https://medium.com/@rdsubhas/docker-for-development-common-problems-and-solutions-95b25cae41eb#.n3bi92f5h


# docker stop problems
- docker stop sends SIGTERM to PID 1
- running several commands run child process so pid 1 does not reach them
https://www.ctl.io/developers/blog/post/gracefully-stopping-docker-containers/
https://github.com/docker/docker/issues/2436
- you could run an sh init file but you have to trap the signal and send it to child processes
http://veithen.github.io/2014/11/16/sigterm-propagation.html


# PM2 Read
https://medium.com/@adriendesbiaux/node-js-pm2-docker-docker-compose-devops-907dedd2b69a#.3j44wdhze

docker stop [OPTIONS] CONTAINER [CONTAINER...]

__Remove Docker Image
docker rmi [OPTIONS] IMAGE [IMAGE...]


__List stopped containers__
docker ps -a

Remove one or more containers
docker rm [OPTIONS] CONTAINER [CONTAINER...]

Remove one or more images
docker rmi [OPTIONS] IMAGE [IMAGE...]

docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)


docker stats


Continuos delivery and stuff
http://dchq.co/


Dockerfiles are pretty neat things. They allow us to do fun stuff, like take someone’s else’s image as a base and build more stuff on top of it. This is the basis for nearly all of the images I use – find someone else who did the hard work, like installing Nginx, or Apache, or a database like Postgres or MySQL, and then add the pieces I need to get the results I want.
