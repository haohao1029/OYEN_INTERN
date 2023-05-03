# OYEN ASSESSMENT LOGIN PAGE WITH FASTAPI

![](assets/demo.gif)

```
OYEN_INTERN
├─ assets
│  └─ demo.gif
├─ backend
│  ├─ .env
│  ├─ database.db
│  ├─ Dockerfile
│  ├─ main.py
│  ├─ Pipfile
│  ├─ Pipfile.lock
│  └─ requirements.txt
├─ docker-compose.yaml
├─ frontend
│  ├─ app
│  │  ├─ index.html
│  │  ├─ login.html
│  │  └─ register.html
│  ├─ Dockerfile
│  └─ nginx
│     └─ default.conf
├─ nginx
│  ├─ default.conf
│  └─ Dockerfile
└─ README.md

```

### How to run
```bash
#port=3050
docker-compose up --build

# OR
#port=5000
# If you want to run the service seperately, you have to update the api call path from
`/api/login` to `localhost:8000/login` in `login.html:37` and `/api/register` to `localhost:8000/register` in `register.html:41`

cd frontend
python3 -m http.server 5000
#port=8000
cd backend
pipenv install -r requirements.txt
uvicorn main:app --reload

# OR
#3000

cd frontend 
docker build oyen_frontend .
docker run -p 3000:3000 oyen_frontend
#8000
cd backend
docker build -t jinghao/oyen_backend .
docker run -it -p 8000:8000 jinghao/oyen_backend
```

## Frontend
Frontend use `localstorage` to store username and you can run straight open the html file or you could use the cmd below to run the file. User will be redirected to home page if user trying to access `/login` and `/register` after they login.


## Backend
all the requirements are stored in `requirements.txt`
You must have sqlite in your laptop in order to run the project. After the project run `database.db` will be created and `users` table with name and password columns will be created if it doesn't exist.
The project use `pipenv` as virtual environment library

## Docker Compose
IN docker compose, the frontend will call `/api/users` but not `localhost:8000/users`, the nginx will be perform `backward proxy` based on the path. You can see the detail at `./nginx/default.conf`

## TODO

- Dockerising multi container with nginx 
