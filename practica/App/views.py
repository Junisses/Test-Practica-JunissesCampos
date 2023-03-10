from django.shortcuts import render
# Create your views here.

from django.views import View
from .models import Cliente, Etapa, Estado, Prospecto, Usuario
from django.http.response import JsonResponse
import json
import requests
from django.http import HttpResponse

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

#CRUD clientes
class CustomerView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id>0):
            customers=list(Cliente.objects.filter(id=id).values())
            if len(customers) > 0:
                customer=customers[0]
                datos = {'message': "Exito", 'clientes':customer}
            else:
                datos = {'message': "Cliente no encontrado..."}
            return JsonResponse(datos)
        else:
            customer = list(Cliente.objects.values())
            if len(customer) > 0:
                datos = {'clientes':customer}
            else:
                datos = {'message': "No hay clientes"}
            return JsonResponse(datos)

    def post(self, request):
        jd = json.loads(request.body)

        if (jd['nombre_empresa']) == "" or (jd['rut']) == "" or (jd['direccion']) == "" or (jd['telefono']) == "" :
            datos = {'message': "No pueden quedar campos vacios"}

        elif len((jd['nombre_empresa'])) >= 50 :
            datos = {'message': "El nombre de empresa supera los 50 caracteres!"}

        elif len((jd['direccion'])) >= 100 :
            datos = {'message': "Abrevia la dirección, esta supera los 100 caracteres"}

        elif len((jd['telefono'])) > 9:
            datos = {'message': "El telefono debe tener 9 digitos"}

        else:
            Cliente.objects.create(nombre_empresa=jd['nombre_empresa'], 
                               rut=jd['rut'], 
                               direccion=jd['direccion'], 
                               telefono=jd['telefono'])
            datos = {'message': "Exito"}

        return JsonResponse(datos)

    
    def put(self, request, id):
        jd = json.loads(request.body)
        customers=list(Cliente.objects.filter(id=id).values())
        if len(customers) > 0:
            customer = Cliente.objects.get(id=id)
            customer.nombre_empresa = jd['nombre_empresa']
            customer.rut=jd['rut']
            customer.direccion=jd['direccion']
            customer.telefono=jd['telefono'] 

            if customer.nombre_empresa == "" or customer.rut == "" or customer.direccion == "" or customer.telefono == "":
                datos = {'message': "No deje campos en blanco"}
            elif len(customer.nombre_empresa) >= 50 :
                datos = {'message': "El nombre de empresa supera los 50 caracteres!"}

            elif len(customer.direccion) >= 100 :
                datos = {'message': "Abrevia la dirección, esta supera los 100 caracteres"}
                
            elif len(customer.telefono) > 9:
                datos = {'message': "El telefono debe tener 9 digitos"}
            else:
                customer.save()
                datos = {'message': "Actualizado con exito"}

        else:
            datos = {'message': "Cliente no encontrado"}
        return JsonResponse(datos)
            
#CRUD Estado
class Prueba(View):
        
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id>0):
            estados=list(Estado.objects.filter(id=id).values())
            if len(estados) > 0:
                estado=estados[0]
                datos = {'message': "Exito", 'estados':estado}
            else:
                datos = {'message': "No existe ese estado..."}
            return JsonResponse(datos)
        else:
            estado = list(Estado.objects.values())
            if len(estado) > 0:
                datos = {'estados':estado}
            else:
                datos = {'message': "No hay estados"}
            return JsonResponse(datos)

    def post(self, request):
        jd = json.loads(request.body)
        if (jd['estado']) == "" :
            datos = {'message': "No pueden quedar campos vacios"}
        elif len((jd['estado'])) >= 8 :
            datos = {'message': "El estado puede tener hasta 8 caracteres"}
        else:
            Estado.objects.create(estado=jd['estado'])
            datos = {'message': "Estado creado"}

        return JsonResponse(datos)
    
    def put(self, request, id):
        jd = json.loads(request.body)
        estados=list(Estado.objects.filter(id=id).values())
        if len(estados) > 0:
            estado = Estado.objects.get(id=id)
            estado.estado = jd['estado']
            if estado.estado == "":
                datos = {'message': "No deje campos en blanco"}
            elif len(estado.estado) >= 8 :
                datos = {'message': "El estado puede tener hasta 8 caracteres"}
            else:
                estado.save()
                datos = {'message': "Actualizado con exito"}

        else:
            datos = {'message': "Estado no encontrado"}
        return JsonResponse(datos)

#CRUD Etapa
class EtapaView(View):
        
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id>0):
            estapas=list(Etapa.objects.filter(id=id).values())
            if len(estapas) > 0:
                etapa=estapas[0]
                datos = {'message': "Exito", 'etapas':etapa}
            else:
                datos = {'message': "No existe esa etapa..."}
            return JsonResponse(datos)
        else:
            etapa = list(Etapa.objects.values())
            if len(etapa) > 0:
                datos = {'etapas':etapa}
            else:
                datos = {'message': "No hay etapas"}
            return JsonResponse(datos)

    def post(self, request):
        jd = json.loads(request.body)
        if (jd['etapa']) == "" :
            datos = {'message': "No pueden quedar campos vacios"}
        elif len((jd['etapa'])) >= 15 :
            datos = {'message': "La etapa puede tener hasta 15 caracteres"}
        else:
            Etapa.objects.create(etapa=jd['etapa'])
            datos = {'message': "Etapa creada"}

        return JsonResponse(datos)
    
    def put(self, request, id):
        jd = json.loads(request.body)
        etapas=list(Etapa.objects.filter(id=id).values())
        if len(etapas) > 0:
            etapa = Etapa.objects.get(id=id)
            etapa.etapa = jd['etapa']
            if etapa.etapa == "":
                datos = {'message': "No deje campos en blanco"}
            elif len(etapa.etapa) >= 15 :
                datos = {'message': "La etapa puede tener hasta 15 caracteres"}
            else:
                etapa.save()
                datos = {'message': "Actualizado con exito"}

        else:
            datos = {'message': "Etapa no encontrada"}
        return JsonResponse(datos)

#CRUD Prospecto
class ProspectoView(View):
        
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id>0):
            prospectos=list(Prospecto.objects.filter(id=id).values())
            if len(prospectos) > 0:
                prospecto=prospectos[0]
                datos = {'message': "Exito", 'prospectos':prospecto}
            else:
                datos = {'message': "No hay prospectos..."}
            return JsonResponse(datos)
        else:
            prospecto = list(Prospecto.objects.values())
            if len(prospecto) > 0:
                datos = {'etapas':prospecto}
            else:
                datos = {'message': "No hay prospectos"}
            return JsonResponse(datos)

    def post(self, request):
        jd = json.loads(request.body)

        try:
            if (jd['nombre']) == "" or (jd['mail']) == "" or (jd['telefono']) == "" or (jd['sexo']) == "" or (jd['cliente_id_id']) == 0 or (jd['estado_id_id']) == 0 or (jd['etapa_id_id']) == 0:
                datos = {'message': "No pueden quedar campos vacios"}
                
            elif len((jd['nombre'])) >= 50 :
                datos = {'message': "El nombre no puede superar los 50 caracteres"}

            elif len((jd['mail'])) >= 100 :
                datos = {'message': "Ups, el email es demasiado extenso, no debe tener mas de 100 caracteres"}

            elif len((jd['telefono'])) > 9 :
                datos = {'message': "El telefono debe contener 9 digitos"}

            elif len((jd['sexo'])) >= 12 :
                datos = {'message': "El sexo no debe tener mas de 12 letras"}
            else:
                Prospecto.objects.create(nombre=jd['nombre'],
                                    mail=jd['mail'],
                                    telefono=jd['telefono'],
                                    sexo=jd['sexo'],
                                    cliente_id_id=jd['cliente_id_id'],
                                    estado_id_id=jd['estado_id_id'],
                                    etapa_id_id=jd['etapa_id_id'])
                datos = {'message': "Prospecto creado"}

        except:
            datos = {'message': "Ups, algo salio mal revisa que las id's ingresadas existan!"}
        return JsonResponse(datos)
    
    def put(self, request, id):
        jd = json.loads(request.body)
        prospectos=list(Prospecto.objects.filter(id=id).values())
        if len(prospectos) > 0:
            prospecto = Prospecto.objects.get(id=id)
            prospecto.nombre = jd['nombre']
            prospecto.mail = jd['mail']
            prospecto.telefono = jd['telefono']
            prospecto.sexo = jd['sexo']
            prospecto.cliente_id_id = jd['cliente_id_id']
            prospecto.estado_id_id = jd['estado_id_id']
            prospecto.etapa_id_id = jd['etapa_id_id']

            try:
                if prospecto.nombre == "" or prospecto.mail == "" or prospecto.telefono == "" or prospecto.sexo == "" or prospecto.cliente_id_id == 0 or prospecto.estado_id_id == 0 or prospecto.etapa_id_id == 0:
                    datos = {'message': "No deje campos en blanco"}

                elif len(prospecto.nombre) >= 50 :
                    datos = {'message': "El nombre no puede superar los 50 caracteres"}

                elif len(prospecto.mail) >= 100 :
                    datos = {'message': "Ups, el email es demasiado extenso, no debe tener mas de 100 caracteres"}

                elif len(prospecto.telefono) > 9 :
                    datos = {'message': "El telefono debe contener 9 digitos"}

                elif len(prospecto.sexo) >= 12 :
                    datos = {'message': "El sexo no debe tener mas de 12 letras"}
                else:
                    prospecto.save()
                    datos = {'message': "Actualizado con exito"}

            except:
                datos = {'message': "Ups, algo salio mal revisa que las id's ingresadas existan!"}
        
        else:
            datos = {'message': "Prospecto no encontrado"}
        return JsonResponse(datos)

#CRUD Usuario
class UsuarioView(View):
        
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id>0):
            usuarios=list(Usuario.objects.filter(id=id).values())
            if len(usuarios) > 0:
                usuario=usuarios[0]
                datos = {'message': "Exito", 'usuarios':usuario}
            else:
                datos = {'message': "No hay usuarios..."}
            return JsonResponse(datos)
        else:
            usuario = list(Usuario.objects.values())
            if len(usuario) > 0:
                datos = {'Usuarios':usuario}
            else:
                datos = {'message': "No hay usuarios"}
            return JsonResponse(datos)

    def post(self, request):
        jd = json.loads(request.body)

        try:
            if (jd['username']) == "" or (jd['password']) == "" or (jd['cliente_id']) == 0 :
                datos = {'message': "No pueden quedar campos vacios"}

            elif len((jd['username'])) >= 15 :
                datos = {'message': "El nombre de usuario supera los 15 caracteres"}

            elif len((jd['password'])) >= 100 :
                datos = {'message': "Ups, contraseña demasiado larga, no debe tener mas de 100 caracteres"}

            else:
                Usuario.objects.create(username=jd['username'],
                                    password=jd['password'],
                                    cliente_id=jd['cliente_id'])
                datos = {'message': "Usuario creado"}

        except:
            datos = {'message': "Ups, algo salio mal revisa que el cliente exista!"}
        return JsonResponse(datos)
    
    def put(self, request, id):
        jd = json.loads(request.body)
        usuarios=list(Usuario.objects.filter(id=id).values())
        if len(usuarios) > 0:
            usuario = Usuario.objects.get(id=id)
            usuario.username = jd['username']
            usuario.password = jd['password']
            usuario.cliente_id = jd['cliente_id']

            if usuario.username == "" or usuario.password == "":
                datos = {'message': "No deje campos en blanco"}

            elif len(usuario.username) >= 15 :
                datos = {'message': "El nombre de usuario supera los 15 caracteres"}

            elif len(usuario.password) >= 100 :
                datos = {'message': "Ups, contraseña demasiado larga, no debe tener mas de 100 caracteres"}

            else:
                usuario.save()
                datos = {'message': "Actualizado con exito"}

        else:
            datos = {'message': "Usuario no encontrado"}
        return JsonResponse(datos)

