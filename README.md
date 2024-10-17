
# RPI Calculator

Technical test

## Installation

Install RPI calculator API with Docker

```bash
  docker-compose up --build
```

## Usage

To use the API start to run this curl command example

```curl
curl -X POST "http://localhost:8000/calculate" -H "Content-Type: application/json" -d '{"expression": "3 4 + 4 * 7 /"}'
```

You can use this curl to run other calcul

Then you can easily run `http://localhost:8000/export_csv` with your browser or tith a curl command

## API Reference

#### POST Expression

```http
  POST /calculate
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `expression` | `string` | Upload an expression and its result |

#### Export all expression in CSV

```http
  GET /export_csv
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `none` | `string` | Download csv file based on the database|

#### Interactiv doc

```http
  GET /docs
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `none` | `string` | Documentation using Swagger|

#### Redoc

```http
  GET /redoc
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `none` | `string` | Documentation using Redoc|
