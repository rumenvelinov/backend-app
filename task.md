The goal is to develop a streamlined CI/CD process for a backend application, incorporating an
SQL database connection.
Optionally, ensuring exposure through Kong Ingress Controller will accrue bonus points.

Minimum requirements:
- Develop a simplistic "Hello World" application using a language of your choice. Dockerize the application, ensuring its operability within a Docker container.
`git checkout 36a5e56d444bda69ed0429b27e2263b9ba72ab55`
`docker build -t backend-app .`
`docker run -d --name app backend-app`
`docker exec -it app curl 127.0.0.1:5000`

- Construct a docker-compose setup to facilitate local development and testing of the application and ensure it's connective operability with an SQL database within the composed environment.
`echo "MYSQL_DATABASE_PASSWORD=yourpass" > .env`
`echo "yourpass" > db_password.txt`
`echo "yourrootpass" > db_root_password.txt`
`docker compose up`
Once mysql is up and running login to the container:
`docker exec -it backend-app-db-1 /bin/bash`
and import db_init.sql into mysql
`127.0.0.1:5000` - should show "Hello, Rumen"

- Configure an automated build and push process for the Docker image using a CI tool (e.g., GitLab CI/CD, GitHub Actions, TravisCI).
`git tag -v1.0.1`
`git push origin v.1.0.1` pushing a tag will start the automatic image build and push

- Deploy your application into a local Kubernetes environment (like kind or minikube), using Helm charts for deployment structuring and management.


- Deploy and manage an SQL database within the Kubernetes cluster using Helm, ensuring that the application can successfully interact with it.
`helm repo add bitnami https://charts.bitnami.com/bitnami`
`helm install --values ./helm/backend-db-custom-values.yaml db bitnami/mysql`