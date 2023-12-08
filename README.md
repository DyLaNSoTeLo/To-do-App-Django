# To-do-App-Django

  
Creacion de un entorno virtual

Abre el CMD y ubícate en la carpeta en donde quieres crear el entorno virtual
Ejecuta python -m venv mi_entorno
Ejecuta mi_entorno\Scripts\activate

Instalacion
Instala el framework djang

pip install django

Instala django-rest-framework

pip install djangorestframework





Empezamos con el proyecto

Creamos el proyecto de nombre tarea_project

django-admin startproject tarea_project

Accedemos dentro de la carpeta del proyecto 

cd tarea_projecto

Creamos una aplicacion dentro del proyecto

python manage.py startapp tarea_app




Ahora dentro en la carpeta tarea_project/settings.py

debemos agregar lo siguiente en INSTALLED_APPS el nombre de nuestra aplicacion

![image](https://github.com/DyLaNSoTeLo/To-do-App-Django/assets/139414515/01bb1696-2642-49e6-9bfb-e05f8eed4352)



Definimos el modelo

En el archivo tarea_app/models.py

![image](https://github.com/DyLaNSoTeLo/To-do-App-Django/assets/139414515/86594a1b-69f6-4126-bb13-f137cb4eea93)


Ahora realizamos las migraciones con los siguientes comando en consola

![image](https://github.com/DyLaNSoTeLo/To-do-App-Django/assets/139414515/04fa4606-bf52-4e5d-99af-62673163f902)


Serializando

Asi que creamos el archivo tarea_app/serializers.py:

![image](https://github.com/DyLaNSoTeLo/To-do-App-Django/assets/139414515/6dc83ecb-fc96-4e00-a5f9-757db9241643)


Vista basada en clase para la API

En el archivo tarea_app/views.py:

![image](https://github.com/DyLaNSoTeLo/To-do-App-Django/assets/139414515/ccec52ac-211d-4a4d-9c18-11112945f7e4)

En esta imagen podemos ver como creamos e implementamos la logica para obtener tareas especificas y para poder crear unas completamente nuevas.

![image](https://github.com/DyLaNSoTeLo/To-do-App-Django/assets/139414515/4a8092b4-9df7-4e0a-adbc-6a46e7407e15)

Aqui como puedes ver, luego de crear las funciones anteriores, creamos clases aplicando la autenticacion para poder acceder a la lista de tareas, y los detalles de una tarea especifica.
Y adicionalmente puedes ver que hace cada funcion revisando los comentarios en el codigo...

Autenticacion basada en token
Proceso de verificar la identidad mediante la comprobación de un token. Un token es un elemento simbólico que expide una fuente de confianza.


Configuración de las URL

Creamos el archivo urls.py dentro de tarea_app, configura las URL para tu vista:

![image](https://github.com/DyLaNSoTeLo/To-do-App-Django/assets/139414515/715a6540-e51d-4e58-b9ec-8faf8d57bbed)

y luego en el archivo urls.py del proyecto:

![image](https://github.com/DyLaNSoTeLo/To-do-App-Django/assets/139414515/78e69714-d1bb-4baa-833a-06374ab74330)

En esta parte vinculamos los urls de nuestra app y el proyecto, a su vez aplicamos los endpoint para la documentacion de nuestra API, y tambien los permisos que tienen los usuarios a la informacion que tenemos dentro de la app.

No sin antes añadir las templates, que previamente definimos en los endpoints.
A continuacion una explicacion grafica de como se pueden estructurar.


Django Templates

Creamos la carpeta templates dentro de tarea_app. 

Ahora tarea_app/templates en donde crearemos nuestros templates con html



tarea_app/templates/base.html

![image](https://github.com/DyLaNSoTeLo/To-do-App-Django/assets/139414515/18a065fe-2024-4c8b-9197-d676f74fd782)

Modificamos los campos necesarios y personalizamos las etiquetas para su vizualizacion en el template.


tarea_app/templates/task_detail.html

![image](https://github.com/DyLaNSoTeLo/To-do-App-Django/assets/139414515/d9443311-cd85-4e0e-8eb4-0ca7024a867a)


tarea_app/templates/task_list.html

![image](https://github.com/DyLaNSoTeLo/To-do-App-Django/assets/139414515/18d59040-c440-4b1a-9719-6a5007445c7d)


tarea_app/templates/task_completed.html

![image](https://github.com/DyLaNSoTeLo/To-do-App-Django/assets/139414515/4761e644-683a-49c2-bdbf-567a15098d94)


Una vez nuestros templates en html tengan la informacion y rutas necesarias, podemos proceder a agregarle estilos a nuestra vista.


Ahora para los estilos creamos la carpeta static dentro de blog tarea_app/static/tarea_app/style.css

![image](https://github.com/DyLaNSoTeLo/To-do-App-Django/assets/139414515/e8b0c1fc-44ae-4d79-8b38-1e8adf483354)

![image](https://github.com/DyLaNSoTeLo/To-do-App-Django/assets/139414515/f4e5bbeb-e0a1-4505-b003-f3ff5af69071)

En esta parte del proyecto debemos priorizar un estilo que sea atractivo para nuesta To do app, y asi mismo la distribucion de los elementos de la misma.


Finalmente ejecutamos en nuestra terminal:  python manage.py runserver.


![image](https://github.com/DyLaNSoTeLo/To-do-App-Django/assets/139414515/6af55771-a6ee-474e-ac4e-55b1f2061e07)


Con esto podremos obtener una url para acceder a todas la vistas de nuestro proyecto, solo debemos escojer la que necesitamos y nos dirigira directamente al endpoint que definimos previamente.

![image](https://github.com/DyLaNSoTeLo/To-do-App-Django/assets/139414515/a84f22ac-f5c3-42ae-ae58-2a9a31c50088)


Tambien usando el endpoint "/admin/", podras acceder al administrador de usuarios y modelos de django restframework.

![image](https://github.com/DyLaNSoTeLo/To-do-App-Django/assets/139414515/c8e7e1f1-b358-492a-9f09-f007553fc23f)

Tambien te dejo una vista previa de lo que seria la vista de las tareas:

![image](https://github.com/DyLaNSoTeLo/To-do-App-Django/assets/139414515/a0828178-2681-43cf-affd-ea73747082f4)

Aqui tenemos el endpoint que nos muestra las tareas que tenemos completadas:

![image](https://github.com/DyLaNSoTeLo/To-do-App-Django/assets/139414515/c5d8aa26-527a-47c0-bbed-d200867ae7b8)

Asi como el endpoint que nos permitira añadir mas tareas, luego de eso, podemos acceder a una tarea especifica y cambiar su estado a completada.

![image](https://github.com/DyLaNSoTeLo/To-do-App-Django/assets/139414515/8a6881a1-1dbe-4688-946c-ca7842e29f50)
























