nikola-saas
===========

Este repositorio es un prueba de concepto, la idea
principal es poder utilizar "nikola" como un servicio
en la nube.

Se ha comenzado esta prueba en pycamp 2012 (Veronica).

Historial de cambios mas importantes
------------------------------------

1. Agregando bootstrap: 08930c03f959c1fb6f132c261e36b5be759ef8cf
2. Templates y acciones usando bootstrap: d5918a909256b00ef440baad708b6992a33fe330
3. Creando formulario para crear sitios: 24a9b6dc392d243d849e73403868325fb9f0d14e
4. Accion crear sitio / bloqueante (comando git): f84128e4d7490660e82f089aa7b9e519accc4015
5. Crear y actualizar sitio, pero ahora con celery: 033e4a8555b1110438098cd7a597fa1dfd7ea271


instalación
-----------


    mkvirtualenv nikola-sass
    workon flaskpastillas
    pip install -r requirements.txt

Es recomendable usar ipython desde virtualenv, aqui hay
instrucciones para configurarlo:

- http://www.ahmedsoliman.com/2011/09/27/use-virtualenv-with-ipython-0-11/

Ejecutar la aplicación en modo desarrollo
-----------------------------------------

Primero hay que entrar en el entorno, y luego
lanzar del servidor de prueba::

    workon nikola-saas
    python app.py


Background process
------------------

El sistema de clonacion de repositorios se realizó usando
Celery, así que si quieres usar esa funcionalidad hay
unos pasos mas...

Primero tienes que iniciar el backend de comunicación:

    redis-server

Luego, desde otro terminal podrías ingresar en el entorno
virtual y lanzar Celery::

    workon nikola-saas
    python manage.py celeryd -c 2 -E

(los parámetros -c 2 y -E permiten que celery solamente use
dos procesos en simultaneo y que se pueda monitorizar de
manera externa).

Para visualizar la cola de trabajos podrías ejecutar en
otra termina:

    workon nikola-saas
    python manage.py celeryev


Juggernaut
----------

Para implementar conexiones persistentes con el servidor
usamos Juggernaut.

Para instalarlo:

    npm install -d juggernaut
    (tal vez necesites instalar nodejs antes)

Luego, para iniciarlo:

    juggernaut

TODO...
