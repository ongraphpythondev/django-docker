# django-docker
- As name suggest, this is Python Django web framework which runs on docker container.
- There is two docker files named **Dockerfile** and **docker-compose.yml**
- There is also django webapp which is blank for further use in django + docker related project.

### Commands needed to run :
- To create root folder/directory in django docker 
```
sudo docker-compose run web django-admin startproject mysite .
```
- To execute django commands while running docker.
```
docker exec django-docker_web_1 python manage.py startapp app
```
```
docker exec django-docker_web_1 python manage.py makemigrations
```
```
docker exec django-docker_web_1 python manage.py migrate
```

- **Note** : All above commonds wil run while docker runs python django server.
- To run django in docker container
```
docker-compose up
```
