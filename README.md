Bienvenidos a mi test ténico de práctica

Junisses Campos ☺

## EJECUCIÓN

➜ Abrir la carpeta en un IDE (recomiendo visual studio code)

➜ Ejecutar terminal dentro del visual code

➜ Instalar lo siguiente:

    ✓ pip install pymysql
    ✓ pip install requests
    
➜ Asegurarse de tener instalado Django y Python, si no se tienen, realizar los siguientes comandos

    ✓ pip install django
    ✓ pip install python
    
➜ Ingresar comando python manage.py migrate para migrar la base de datos
  (Algunas veces no me reconoce el HOST, por lo que voy a settings.py y en la línea 85 le cambio lo que esta entre las comillas. Para saber por cual cambiarle utilizo    ubuntu que esta conectado a docker directamente, y con el comando "dig mysql" veo cual es la IP, normalmente aparece en la línea que dice "SERVER", damos a guardar    y volvemos a ejecutar este código, cuando nos aparece que la migración fue exitosa u ok, continuamos)

➜ Crear super usuario con python manage.py createsuperuser

➜ Correr docker-compose up -d

➜ Luego de hacer esto, podemos ingresar a http://localhost:8000/admin/ e ingresar con las credenciales creadas en el super usuario

En este punto ya esta funcionando la aplicación, por lo que para probar las apis creadas, se puede hacer desde POSTman o desde el mismo visual studio code, instalando una extesion llamada "REST client", con este podemos ir a una carpeta dentro del proyecto llamada "prueba_api", abrimos los archivos http...

![image](https://user-images.githubusercontent.com/55362940/224223810-bcfbf4ad-60dc-43e2-bcfe-b76209550db8.png)


Y seleccionamos el Send Request para ver el resultado de las apis realizadas☻


## EJECUCIÓN MEDIANTE ENTORNO VIRTUAL

Realice un entorno virtual "carpeta venv" para poder instalar algunos elementos, como lo es pymysql, requests, entre otros, y no tener la necesidad de instalarlos directamente en el pc, por si estas usando otras versiones de los programas.

  ➜ Abrir carpeta en el IDE
  
  ➜ Ejecutar terminal
  
  ➜ Ingresar al entorno virtual con ./venv/Scripts/activate
  
  ➜ Migrar los datos con python manage.py migrate, para que se llene la base de datos 
    (Algunas veces no me reconoce el HOST, por lo que voy a settings.py y en la línea 85 le cambio lo que esta entre las comillas. Para saber por cual cambiarle            utilizo ubuntu que esta conectado a docker directamente, y con el comando "dig mysql" veo cual es la IP, normalmente aparece en la línea que dice "SERVER", damos      a guardar y volvemos a ejecutar este código, cuando nos aparece que la migración fue exitosa u ok, continuamos)

  ➜ Correr docker-compose up -d

  ➜ Creamos un super usuario python manage.py createsuperuser
  
  ➜ Finalmente, lo mismo que el punto anterior, se pueden ver las apis en la carpeta "prueba_api", de igual manera si esto se ejecuta por url, por ejemplo  http://localhost:8000/app/clientes/, se listarán los clientes en un .json o su respectivo mensaje de error en caso de no tener clientes aún ingresados.


  
