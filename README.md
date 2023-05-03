# OYEN ASSESSMENT LOGIN PAGE WITH FASTAPI

![](assets/demo.gif)


### How to run
```bash
docker-compose up --build
# OR 

cd frontend
python3 -m http.server 5000

cd backend
pipenv install -r requirements.txt
uvicorn main:app --reload

# OR

cd frontend 
docker build oyen_frontend .
docker run -p 3000:3000 oyen_frontend

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


## TODO

- Dockerising multi container with nginx 

