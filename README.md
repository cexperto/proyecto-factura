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