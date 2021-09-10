## Notes
```create_fake_data.py``` script provides an easy way to insert some data to test endpoints. Just need run migration corresponding before run this script.

```Docker``` option is the best way to test and deploy this app. Only needs (copy and paste) two commands and that's it!

## Task requirements

<ul>
    <li>
        Crear una aplicación para estudiantes que contenga un modelo Estudiante, una vista para listar los estudiantes en la base de datos y poder acceder al detalle de cada estudiante.
    </li>
    <li>
        Además crear un modelo para Clase, y una vista para poder ver la lista de clases disponibles.
    </li>
</ul>

## Docker instructions
```
# build image
    docker build -t django-app .
# run container
    docker run -it -p 8000:8000 django-app
```

Open your browser at: ```localhost:8000/students/``` or ```localhost:8000/courses/```

## Endpoints
```
COURSES:
   courses/
   courses/<pk>/
STUDENTS:
   students/
   students/<pk>/
```

## Project  structure
```
|_ courses/
    |_ [..]
|_ schoolmanagement/
    |_ [..]
|_ students/
    |_ [..]
```