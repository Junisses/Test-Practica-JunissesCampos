Bienvenidos a mi test ténico de práctica

Realice un entorno virtual "carpeta venv" para poder instalar algunos elementos, como lo es pymysql, requests, entre otros.
Este sistema se puede ejecutar de dos maneras, una es dentro del entorno virtual, y para ello debemos realizar lo siguiente:
  > Abrir carpeta (recomiendo usar visual studio code)
  > Ejecutar terminal
  > Ingresar al entorno virtual con ./venv/Scripts/activate
  > Correr docker-compose up -d
  > Migrar los datos con python manage.py migrate, para que se llene la base de datos (Algunas veces no me reconoce el HOST, por lo que voy a settings.py y se lo cambio por la ip que da docker al escribir dig mysql)***************
  > Creamos un super usuario python manage.py createsuperuser
  > Luego de hacer esto, podemos ingresar a http://localhost:8000/admin/ e ingresar con las credenciales creadas
En este punto ya esta funcionando la aplicacion, por lo que para probar las apis creadas, se puede hacer desde POSTman o desde el mismo visual studio code, instalando una extesion llamada "REST client", con este podemos ir a una carpeta dentro del proyecto llamada "prueba_api", abrimos los archivos http...
![image](https://user-images.githubusercontent.com/55362940/224223810-bcfbf4ad-60dc-43e2-bcfe-b76209550db8.png)


