			info = Persona.objects.filter(cedula=request.POST.get("cedula"))
			#print request.POST.get("cedula")
			if len(info) == 0:

				if request.POST.get("es_cliente"):
					es_cliente = True
					#print "cliente activo"
				else:
					es_cliente = False
					#print "cliente off"

				if request.POST.get("es_testigo"):
					es_testigo = True
					#print "testigo activo"
				else:
					es_testigo = False
					#print"testigo off"

				upload = UploadForm(request.POST, request.FILES)
				if upload.is_valid():
					print "hay foto"
					foto= request.FILES['foto']
				else:
					print "no hay foto"
					foto= None

				if request.POST.get("fecha_nacimiento") == "":
					fecha_nac=None
				else:
					fecha_nac = request.POST.get("fecha_nacimiento")

				informacion = Persona(
					cedula=request.POST.get("cedula"), 
					nombres=request.POST.get("nombres"),
					apellidos = request.POST.get("apellidos"),
					ciudad= request.POST.get("ciudad"),
					direccion= request.POST.get("direccion"),
					telefono= request.POST.get("telefono"),
					celular= request.POST.get("celular"),
					es_cliente= es_cliente,
					es_testigo= es_testigo,
					fecha_nacimiento= fecha_nac,
					foto= foto,
					usuario= request.user)
 				informacion.save()
				response_data['message'] = 1	# Datos guardados satisfactoriamente
				return HttpResponse(json.dumps(response_data), content_type="application/json")
			else:
				response_data['message'] = 2	# la persona ya existe
				return HttpResponse(json.dumps(response_data), content_type="application/json")
