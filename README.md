
# Django Rest Framework

Simple Django CRUD API With JWT Authentication and multiple roles

## Run Locally

Clone the project

```bash
  git clone https://github.com/abdulfh/django-simple-crud
```

Go to the project directory

```bash
  cd django-simple-crud
```

Run Docker

```bash
  docker-compose build && docker-compose up
```
## Register Admin & User

#### Register Admin 

```http
  POST /auth/admin/register
```

| Parameter | Type     | Required |
| :-------- | :------- | :------- |
| `email` | `string` | **Yes**|
| `password` | `string` | **Yes**|

#### Register User 

```http
  POST /auth/user/register
```

| Parameter | Type     | Required | 
| :-------- | :------- | :------- |
| `username` | `string` | **Yes**|
| `email` | `string` | **Yes**|
| `password` | `string` | **Yes**|
| `phoneNumber` | `string` | **Yes**|
| `city` | `string` | **Yes**|
| `zip` | `string` | **Yes**|
| `message` | `string` | **Yes**|
| `address` | `string` | **Yes**|

