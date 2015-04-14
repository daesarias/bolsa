# -*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
#importar modelos en caso de necestiar
from django.template import RequestContext
from django.utils import timezone
from django.contrib.auth.decorators import login_required
import json
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse

from Appi.models import Usuario
from django.core.mail import send_mail
import smtplib



@login_required
def Principal(request):	#pagina de inicio
	return render_to_response('usuario/principal.html', context_instance=RequestContext(request))#[template_directory]/pregrep/index.html


@login_required
def Listar_solicitudes(request):
        if request.user.is_staff:
                usuarios = Usuario.objects.all()
                return render_to_response('usuario/listarUsuarios.html',{'usuarios': usuarios}, context_instance=RequestContext(request))#[template_directory]/pregrep/index.html

@login_required
def Cambiar_estado_usuario(request):
        if request.user.is_staff:
                print 'entre'
                estado= request.POST['estado']
                numero= request.POST['usuario']
                perfil = request.POST['perfil']
                print perfil
                response_data = {}
                cliente = get_object_or_404(Usuario, numero=numero)
                #mensaje='Reciba un caluroso saludo de nuestra parte; permítanos informarle que su cuenta de usuario en bolsaEmpleo.com se encuentra'
                if estado == 'Aprobado':
                        cliente.estado='Aprobado'
                        cliente.perfil=perfil
                        cliente.usuario.is_active=True
                        cliente.usuario.save()
                        cliente.save()
                        
                        response_data['message'] = 1	# Datos guardados satisfactoriamente
                        #aqui se debe enviar el correo electronico
                elif estado == 'Rechazado':
                        cliente.estado='Rechazado'
                        cliente.perfil=perfil
                        
                        print cliente.usuario.is_active
                        cliente.usuario.is_active =False
                        cliente.usuario.save()
                        cliente.save()
                        
                        response_data['message'] = 1	# Datos guardados satisfactoriamente
                        #aqui se debe enviar el correo electronico

                elif estado == 'En espera':
                        cliente.estado='En espera'
                        cliente.perfil=perfil
                        cliente.usuario.is_active=False
                        cliente.usuario.save()
                        cliente.save()

                        response_data['message'] = 1	# Datos guardados satisfactoriamente
                        #aqui se debe enviar el correo electronico

                print 'por aca llego la baina'
                print cliente.usuario.username
                send_mail('Estado de su cuenta en bolsaEmpleo.com','actualmente su cuenta se encuentra en estado: '+estado, 'bolsaempleo28gmail.com', [cliente.usuario.username], fail_silently=False)                       
                return HttpResponse(json.dumps(response_data), content_type="application/json")
         
               
