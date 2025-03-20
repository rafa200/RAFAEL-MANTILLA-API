# API de Personas con Flask

## Descripción
Este proyecto es una API sencilla creada con Flask que proporciona un endpoint para obtener una lista de personas en formato JSON.

La API estará disponible en `http://127.0.0.1:5000/personas`.

## Endpoints

### `GET /personas`
Devuelve la lista de personas en formato JSON.

#### Respuesta Ejemplo:
```json
[
    {"id": 1, "nombre": "Juan Perez", "edad": 30},
    {"id": 2, "nombre": "Maria Lopez", "edad": 25}
]
```

## Configuración
Si necesitas modificar la lista de personas, edita el archivo `datos/personas.py`.

## Contribución
Si deseas contribuir, sigue estos pasos:
1. Haz un fork del repositorio.
2. Crea una nueva rama:
   ```bash
   git checkout -b mi-rama
   ```
3. Realiza tus cambios y confírmalos:
   ```bash
   git commit -m "Agregado nuevo feature"
   ```
4. Sube tus cambios a tu fork:
   ```bash
   git push origin mi-rama
   ```
5. Crea un Pull Request en GitHub.

