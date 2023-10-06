# metacritic-api

## Runs in a docker file
Requires python 3.8.x
## Running the api in docker

```sh
docker build -t python-api .
```

```sh
docker run -d -ti -p 8080:8080 --name python-api python-api
```

navigate to http://127.0.0.1:8080/games
