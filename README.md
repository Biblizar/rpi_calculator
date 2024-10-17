
# RPI Calculator

Technical test

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


#### Export all expression in CSV
```http
  GET /docs
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `none` | `string` | Documentation using Swagger|
