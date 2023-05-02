# OYEN ASSESSMENT LOGIN PAGE WITH FASTAPI

![](assets/demo.gif)

```
OYEN_INTERN
├─ backend
│  ├─ .env
│  ├─ config.py
│  ├─ database.db
│  ├─ main.py
│  ├─ Pipfile
│  ├─ Pipfile.lock
│  └─ requirements.txt
├─ frontend
│  ├─ index.html
│  ├─ login.html
│  └─ register.html
└─ README.md

```

## Frontend
Frontend use `localstorage` to store username and you can run straight open the html file or you could use the cmd below to run the file. User will be redirected to home page if user trying to access `/login` and `/register` after they login.
```
python3 -m http.server 5000
```

## Backend
all the requirements are stored in `requirements.txt`
You must have sqlite in your laptop in order to run the project. After the project run `database.db` will be created and `users` table with name and password columns will be created if it doesn't exist.
The project use `pipenv` as virtual environment library
### How to run
```bash
pipenv install -r requirements.txt
uvicorn main:app --reload
```

## TODO

- Dockerising multi container with nginx 
