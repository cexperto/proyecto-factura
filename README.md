# Factura

Una app para creacion de facturas

## Installation

Tener docker compose

```bash
  sudo docker-compose -f local.yml build
  sudo docker compose -f local.yml up
  docker compose -f local.yml run --rm django python manage.py migrate  
  
```

    
## Deployment

http://0.0.0.0:8000/


## tests

```bash
  docker compose -f local.yml run --rm django pytest  
  
```


## api

GET

http://0.0.0.0:8000/api-listar-facturas/


POST

{"nombre_cliente":"prueba api",
"fecha_emision":"2023-11-01",
"nombre_producto":"car",
"cantidad":12,
"precio_unitario":"255.00"
}