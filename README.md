# Python Song Machine

Test creado con **Python (Django, Django Rest Framework)**


## 1. Características principales

De esta forma el sistema da solución a los problemas presentados en la prueba.

- **Enpoint para buscar canciones:**

Primero se deben importar las canciones del JSON a la base de datos mediante la petición GET a:

```
  GET  /api/import
```

Con ayuda de Django Rest Framework se desarrolló una vista que 
consulta los datos importados y con la extención de filtros instalada
_django_filters_ permite buscar en canciones en este caso por titulo de la canción.

***Buscar por titulo***:

Usando el endpoint por método GET y enviando como parámetro el nombre de la canción.
Obtiene la respuesta de las canciones filtradas por ese titulo.

```
GET /api/songs?title=Super Gremlin
```

***Buscar por nombre artista:***:

Usando el endpoint por método GET y enviando como parámetro el nombre del artista.
Obtiene la respuesta de las canciones filtradas que coincidan con ese artista.

```
GET /api/songs?artist__name=Kodak Black
```

- **Endpoint para mostrar el TOP 50 de canciones:**

Con ayuda de Django Rest Framework se crea la vista TopSongList que permite 
hacer un RAW SQL (Bonus SQL select).
Para usar este servicio se enviá por GET la siguiente ruta.

```
GET /api/songs/top
```

- **Endpoint para eliminar canción:**

Con la vista ViewSet se crea el método Delete que envia un parametro con un ID existente en la lista 
de canciones importadas. Cuando se enviá esta petición se eliminara la canción requerida y retorna un estado 200.

```
DELETE /api/song/<id_de_la_canción>
```

- **Enpoint para crear nueva canción:**

Con Django Rest Framework se crea un serializer nuevo para insertar canciones con sus elementos relacionados.
Una vez el usuario del enpoint enviá un JSON con una estructura valida y usando códigos de artistas y géneros existentes en la base de datos se crea la canción.

usando el método POST y enviando un JSON con la siguiente estructura.

```
POST /api/songs/top
```

```
{
    "title": "TITLE NEW SONG",
    "release_date": "2021-10-30",
    "explicit": true,
    "artist": 1053,
    "genres": [6]
}
```

***Insertar varios generos***
```
POST /api/songs/top
```

```
{
    "title": "TEST SONG",
    "release_date": "2021-10-30",
    "explicit": true,
    "artist": 1053,
    "genres": [6, 14]		
}
```

**BONUS**

. Mediante la App Imports se consulta la API de canciones y mediante una inserción masiva optima
para Django y a través del ORM se lleva a los esquemas de bases de datos en SQLITE (db.sqlite3)

.  Todas las peticiones excepto la de importar deben autenticarse mediante Token de usuario de Django Rest Framework.
Para ello deberá crear un usuario y a este crearle un Token (Más adelante en el proceso de instalación se indicara como hacerlo).

En los headers de las peticiones.

```
Authorization: Token <Token de usuario>
```

. Para la consulta del TOP 50 de canciones como Django Rest Framework debe recibir 
un Queryset para funcionar se simula mediante un RAWSQL la consulta con lenguaje SQL.

Este método lo podrá encontrar en el modelo Song en el método *select_raw_top* y se verá implementado en 
las vistas del mismo.

- Con la ayuda del Socializador de géneros se pudo agrupar cada genero y dentro de ellos 
las canciones que tengan relación con cada genero y esta retornará un JSON con dicha estructura.

Para ello se creó el endpoint genders group.
```
GET /api/genders
```

## Estructura de Código :


Para este aplicativo se usa la estructura  de Django (basada en MVT). Donde cada aplicativo
tienen buenas practicas de código como la implementación de formato PEP8,
las vistas tienen el menor código posible, se distribuye en clases y funciones con unicas responsabilidades,  la lógica está en otros módulos.

. **Estructura proyecto**

```

    - /imports
        -- services.py  Contiene los métodos de importación.
        -- test.py contiene los casos de prueba para la APP imports
        -- views.py contiene el Endpoint.
    - /python_song_machine contiene la configuración del proyecto  
    - /Songs
        -- models.py  Contiene los modelos de esquemas y vistas para los endpoints.
        -- urls.py contiene las rutas url de los endpoints.
        -- serializers.py Contiene los serializadores de modelos para retornar los datos JSON.
        -- views.py vistas que implementan modelos y serializadores.
    db.sqlite3
    requirements.txt

```

## Instalación:

Una vez clonado el proyecto con el sistema e versiones **git** y idealmente teniendo el ambiente virtual creado ,con el sistema paquetes de python **pip**. se instalan 
las dependencias faltantes asociadas al proyecto que se encuentran en el archivo **requirements.txt**.

```
pip install -r requirements.txt 
```

###  Migración esquemas base de datos

Una vez configurado el proyecto en general procedemos a hacer la migración inicial para dejar funcionando la base de datos.
Todo esto con ayuda del asistente de Django y el ambiente virtual activado.

```
python manage.py migrate
```

### Creacion de usuario y tokens de seguridad.
Una vez estén configurados los puntos anteriores debes tener tu usuario en el sistema.
con el siguiente comando asignaras un nombre de usuario y contraseña.

```
python manage.py createsuperuser
```

### Pruebas unitarias

con la ayuda del asistente de Django podemos ejecutar el comando para correr las pruebas.
Esto se hace necesario si quieres ejecutar las pruebas dedicadas a los imports.

```
python manage.py test
```

Con el usuario recién creado procedemos a crear el token de seguridad que servirá para 
autenticar los endpoints. 

**Nota:** 
- sin estas autenticaciones no tendremos acceso a los endpoints.
- el comando para generar el token funcionara con django rest framework instalado. Importante el proceso de migración.

### Puesta en marcha:

Con todos los pasos anteriores listos la aplicación estará lista para funcionar.
Ejecutando el siguiente comando.

```
python manage.py runserver
```