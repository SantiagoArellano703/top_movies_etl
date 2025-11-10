# Movies ETL

Este proyecto es un servicio web ETL (Extracción, Transformación y Carga) construido con FastAPI. Su propósito es extraer datos de películas desde una plataforma, transformarlos a un formato limpio y consistente, y exportarlos como un archivo CSV.

## 🌟 Características

- **Extracción de Datos**: Obtiene datos de películas desde diferentes fuentes.
- **Transformación de Datos**: Limpia y estandariza la información extraída.
- **Exportación a CSV**: Guarda los datos procesados en un archivo CSV.
- **Arquitectura Hexagonal**: La lógica de negocio está desacoplada de los servicios externos.
- **API Sencilla**: Un único endpoint para iniciar todo el proceso.

## 🏗️ Arquitectura

El proyecto sigue los principios de la **Arquitectura Hexagonal** (también conocida como Puertos y Adaptadores). Esto permite una clara separación de responsabilidades:

- **`src/core`**: Contiene la lógica de negocio pura (dominio y casos de uso), sin dependencias de frameworks o servicios externos.
- **`src/adapters`**: Contiene las implementaciones concretas que interactúan con el mundo exterior (API, scrapers, exportadores).

## 🚀 Cómo Empezar

Sigue estos pasos para configurar y ejecutar el proyecto en tu entorno local.

### Prerrequisitos

- Python 3.8 o superior
- pip

### Instalación

1. Clona el repositorio:
   ```bash
   git clone git@github.com:SantiagoArellano703/top_movies_etl.git
   cd movies_etl
   ```

2. (Opcional pero recomendado) Crea y activa un entorno virtual:
   ```bash
   python -m venv venv
   # En Windows
   venv\Scripts\activate
   # En macOS/Linux
   source venv/bin/activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

### Ejecución

1. Inicia el servidor de desarrollo:
   ```bash
   uvicorn src.app:app --reload
   ```
   El servidor estará disponible en `http://127.0.0.1:8000`.

## 🔌 API Endpoints

La aplicación expone un único endpoint para controlar el proceso ETL.

### `POST /download`

Inicia el proceso de extracción, transformación y exportación de datos de películas.

**Request Body:**

```json
{
  "platform": "tmdb",
  "limit": 100
}
```

- `platform` (str): La plataforma desde la cual extraer los datos. Actualmente, `"tmdb"` es una opción soportada.
- `limit` (int): El número de películas a procesar.

**Respuesta Exitosa:**

- **Código**: `200 OK`
- **Body**: El endpoint devuelve un archivo `movies.csv` para descargar, que contiene los datos de las películas procesadas.

Puedes acceder a la documentación interactiva de la API (generada por Swagger UI) en `http://127.0.0.1:8000/docs` para probar el endpoint directamente desde tu navegador.
