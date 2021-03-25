# Content-Management-System
Django REST framework demo app

## Installation
### On local machine

```bash
pip install -r requirements.txt
python manage.py migrate
```

### Create superuser and runserver
```bash
python manage.py createsuperuser
python manage.py runserver
```

### Login with superuser 
`POST http://localhost:8000/login`

## API overview
### Create new user
```
POST /api/user

{
  "full_name": "Jane Doe",
  "email": "jane@email.com",
  ...
}
```

### List all users
`GET /api/user`

### Retrieve specific user
`GET /api/user/<int:pk>`

### Create new content
```
POST /api/content

{
  "title": "Resume",
  "body": "Application for Developer role",
  ...
}
```

### List all contents
`GET /api/content`

### Retrieve specific content
`GET /api/content/<int:pk>`

### Update specific content
```
PATCH /api/content/<int:pk>

{
  "title": "New title",
  "summary": "Lorem ipsum",
}
```






