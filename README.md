
![image](https://user-images.githubusercontent.com/60367971/127914569-33b1a64b-2fc5-4085-8849-cbbdc85f41fa.png)
    
# Flink - API REST 

A rest api that shows a form with the following data and generates the crud with its corresponding validations

## Tech Stack

**Server:** Python, Django, Docker, Nginx

## Warning -

It is necessary not to have port **80**, **8080**, **5050**, **5432** in use

  
  
## Demo

link to demo
> swagger http://143.198.58.196/
> admin http://143.198.58.196:5050/
- credential admin database


> root@admin.com
> root


  
## Screenshots

![App Screenshot](https://user-images.githubusercontent.com/60367971/127915700-02b1b989-b6b6-417e-83e4-70dcbc513b1e.png)

## Run Locally

Clone the project

```bash
  git clone https://github.com/Esteban1891/Flink---API-REST-.git
```

Go to the project directory

```bash
  cd API_REST_Flink
```

Install Docker

Start the server

```bash
docker-compose up --build  --remove-orphans
```


After installing we run the application in python / django to lift the application

- Be sure to open another terminal in the working directory and run these commands one by one
```bash
1. docker-compose run backend python backend/manage.py collectstatic

2. docker-compose run backend python backend/manage.py makemigrations

3. docker-compose run backend python backend/manage.py migrate
```
  
# Test
open other terminal and write next
```
❯ docker exec -it  prueba-tecnica-flink_backend_1 bash 
❯ cd backend
❯ python manage.py test

show> ...
----------------------------------------------------------------------
Ran 3 tests in 0.140s

OK
```

  
## API Reference

#### Get all items

```http
  GET http://127.0.0.1/api/v1/formulary/

```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `None` | `string, integer` | **Required**. api to get all formulary |

#### Post item

```http
  POST http://127.0.0.1/api/v1/formulary/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name_company, description_company, symbol, market_values`      | `string, array, integer` | **Required**. fiel of item to fetch |


#### Get item

```http
  GET http://127.0.0.1/api/v1/formulary/{id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id, name_company, description_company, symbol, market_values`      | `uuid` | **Required**. Id of item to fetch |


#### PUT item id

```http
  PUT http://127.0.0.1/api/v1/formulary/{id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id, name_company, description_company, symbol, market_values`      | `uuid` | **Required**. Id of item to fetch |

#### DELETE item id

```http
  DELETE http://127.0.0.1/api/v1/formulary/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id, name_company, description_company, symbol, market_values`      | `uuid` | **Required**. Id of item to fetch |



Takes two numbers and returns the sum.

  
## Authors

- [@Esteban1891](https://www.github.com/Esteban1891)

  
## License

[MIT](https://choosealicense.com/licenses/mit/)

  
## Used By

This project is used by the following companies:

- Flink

  
## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://estebandelahoz.me/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/estebandelahoz/)

  
