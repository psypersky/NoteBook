# Setting up python projects

## Docker

It is important to note that by default Alpine uses musl instead of glibc by default. This means that some Python wheels won’t work without forcing a recompilation. ??

// 
https://blog.realkinetic.com/building-minimal-docker-containers-for-python-applications-37d0272c52f3

## Virtual environments

TODO: https://medium.com/swlh/a-guide-to-python-virtual-environments-8af34aa106ac

## venv/virutalenv in Docker

Is it worth it? :/

https://pmac.io/2019/02/multi-stage-dockerfile-and-python-virtualenv/
https://vsupalov.com/virtualenv-in-docker/