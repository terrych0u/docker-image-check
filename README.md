
This image use to check running container on the machine, it's images have update on docker hub or not.
It base on python:2.7.14-alpine and following step to check:

```text
1. Using python library for the Docker Engine API to get container's ID , Repo , Tag
2. Call the Docker Hub API to verify Digest on Docker Hub and local images
3. If Digest dosen't match , it will print "true"
```

## Requirements
In order to build it you need the following python components in your system.
Which you can use "pip install", and this image will install for you.

```text
1.docker (docker-py, Docker SDK for Python)
2.request (simple HTTP library for Python)
```

## Usage
Following step to build and run this image:

1.Give it an name and build image  <br /> 
ex:
```text
docker build -t=app .
```
2.Mount `docker.sock` that on the host machine into container and run it   <br />
ex:
```text
 docker run -it -v /var/run/docker.sock:/var/run/docker.sock app
```
3.It will print the result on the console   <br />
ex:
```text
CONTAINER ID      TAG       UP TO DATE?
80467697c3       latest     true
f936e4b7f4   2.7.14-alpine  false
a342ee5104       latest     false
55c3b2f6e5   20170621-1645  Not Found in Docker Hub
5ac4e10612   20170825-1223  Not Found in Docker Hub
3cb9c78b56        3.4       false
314ea8078c       latest     true
```
