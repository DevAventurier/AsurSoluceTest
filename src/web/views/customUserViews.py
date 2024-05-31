from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core import serializers
from django.shortcuts import HttpResponse, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings

from api.models.departement import Department
from web_front_end.forms.department_form import DepartmentForm
from api.serializers.department_serializer import DepartmentSerializer
from tablib import Dataset
import os

ROOT_FOLDER = "departments"
INDEX_PATH = f"{ROOT_FOLDER}/index.html"
FORM_PARTIAL_PATH = f"{ROOT_FOLDER}/form-modal-partial.html"

@login_required(login_url=settings.LOGIN_URL)
def index(request):
    data = {
        "title" : "departments",
        "model_name": "department"
    }
    return render(request, INDEX_PATH, context=data)

@login_required(login_url=settings.LOGIN_URL)
def department_list(request):
    departements = Department.objects.all().order_by('-id')
    departements_serializer = DepartmentSerializer(departements, many=True).data
    data = {"departments": departements_serializer}
    return JsonResponse(data)

@login_required(login_url=settings.LOGIN_URL)
def department_create(request):
    data = {}
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        form_is_valid = form.is_valid()
        if form_is_valid:
            department = form.save()
            data['message'] = f"Le département {department.name} a été ajouté avec succes !"
        data['form_is_valid'] = form_is_valid
    else:
        form = DepartmentForm()
    context = {
        'form': form,
        'title' : "Create department"
    }
    data['html_form'] = render_to_string(
        FORM_PARTIAL_PATH,
        context,
        request=request,
    )
    return JsonResponse(data)

@login_required(login_url=settings.LOGIN_URL)
def department_update(request, id):
    data = {}
    departement = get_object_or_404(Department, pk=id)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=departement)
        form_is_valid = form.is_valid()
        if form_is_valid:
            form.save()
            data['message'] = f"Le département {departement.name} a été mis à jour avec succes !"
        data['form_is_valid'] = form_is_valid
    else:
        form = DepartmentForm(instance=departement)
        
    context = {
        'form': form,
        'title' : f"Update department {departement.name}"
        }
    data['html_form'] = render_to_string(
        FORM_PARTIAL_PATH,
        context,
        request=request,
    )
    return JsonResponse(data)

@login_required(login_url=settings.LOGIN_URL)
def department_delete(request, id):
    department = get_object_or_404(Department, pk=id)
    department.delete()
    message = f"Le département {department.name} a été bien supprimé !"
    data = {
        "message" : message
    }
    return JsonResponse(data)

@login_required(login_url=settings.LOGIN_URL)
def department_import(request):
    if request.method == "POST":
        file = request.FILES.get('file')
        if file:
            dataset = Dataset()
            rows = dataset.load(file.read(), format="xlsx")
            for row in rows:
                Department.objects.get_or_create(name=row[0])
        return JsonResponse(data={"message": "Les départements on été importer avec success."})
    
    file_path = "media/excel/template_departments.xlsx"
    with open(file_path, 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
        return response





