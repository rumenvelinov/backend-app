# backend-app

Simple hello world app using Python and Flask.

## How to use it?

* Build a image:
`docker build -t backend-app .`
* Run a container:
`docker run -d --name app backend-app`
* Test it's working(should return "Home"):
`docker exec -it app curl 127.0.0.1:5000`
