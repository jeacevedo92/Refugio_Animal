from django.shortcuts import render, redirect
from apps.mascota.forms import MascotaForm
from apps.mascota.models import Mascota

def index(request):
    return render(request, 'mascota/index.html')

#Agregar mascota
def mascota_view(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            print(form)
            form.save()
        #return redirect('mascota_crear')
    else:
        form = MascotaForm()
    mensaje = "sebasesgay"
    return render(request, 'mascota/agregar_mascota.html', {'form': form,'mensaje':mensaje})

#Listar mascotas
def mascota_list(req):
    mascota  = Mascota.objects.all().order_by('id')
    contexto = {'mascotas':mascota}

    return render(req,'mascota/mascota_list.html',contexto)

#editar mascotas
def mascota_edit(req, id_mascota):
    mascota  = Mascota.objects.get(id=id_mascota)
    if req.method == 'GET':
        form = MascotaForm(instance=mascota)
    else:
        form = MascotaForm(req.POST, instance=mascota)
        if form.is_valid():
            form.save()
        return redirect('mascota_listar')
    return render(req, 'mascota/agregar_mascota.html', {'form': form} )

def mascota_delete(req, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if req.method == 'POST':
        mascota.delete()
        return redirect('mascota_listar')
    return render(req, 'mascota/mascota_delete.html',{'mascota':mascota})
