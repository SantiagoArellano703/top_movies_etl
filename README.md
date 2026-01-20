# Movies ETL

Este proyecto es un servicio web ETL (Extracción, Transformación y Carga) construido con FastAPI. Su propósito es extraer datos de películas desde una plataforma, transformarlos a un formato limpio y consistente, y exportarlos como un archivo CSV.

## Características

- **Extracción de Datos**: Obtiene datos de películas desde diferentes fuentes.
- **Transformación de Datos**: Limpia y estandariza la información extraída.
- **Exportación a CSV**: Guarda los datos procesados en un archivo CSV.
- **Arquitectura Hexagonal**: La lógica de negocio está desacoplada de los servicios externos.
- **API Sencilla**: Un único endpoint para iniciar todo el proceso.

## Arquitectura

El proyecto sigue los principios de la **Arquitectura Hexagonal** (también conocida como Puertos y Adaptadores). Esto permite una clara separación de responsabilidades:

- **`src/core`**: Contiene la lógica de negocio pura (dominio y casos de uso), sin dependencias de frameworks o servicios externos.
- **`src/adapters`**: Contiene las implementaciones concretas que interactúan con el mundo exterior (API, scrapers, exportadores).

### Instalación

1. Clona el repositorio:
   ```bash
   git clone git@github.com:SantiagoArellano703/top_movies_etl.git
   cd movies_etl
   ```

2. Crea la imagen de docker:
   ```bash
   docker build -t movies-etl .
   ```

### Ejecución

1. Ejecuta el contenedor para iniciar el servidor::
   ```bash
   docker run -p 8000:8000 movies-etl
   ```
   El servidor estará disponible en `http://127.0.0.1:8000`.

## API Endpoints

La aplicación expone un único endpoint para controlar el proceso ETL.

### `POST /api/top-movies/download`

Inicia el proceso de extracción, transformación y exportación de datos del top de películas.

**Request Body:**

```json
{
  "platform": "tmdb",
  "output_filename": "top_movies",
  "limit": 50
}
```

- `platform` (str): La plataforma desde la cual extraer los datos. Actualmente, `"tmdb"` es una opción soportada.
- `output_filename` (str): Nombre del archivo de salida.
- `limit` (int): El número de películas a procesar.

**Respuesta Exitosa:**

- **Código**: `200 OK`
- **Body**: Archivo CSV descargable con los datos procesados.

Puedes acceder a la documentación interactiva de la API (generada por Swagger UI) en `http://127.0.0.1:8000/docs` para probar el endpoint directamente desde tu navegador.
