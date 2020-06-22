from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json
from ..service.StudentService import *

stu_service = StudentService()


@require_http_methods(["POST"])
def insert_student(request):
    response = {}
    try:
        sid = int(request.POST.get('sid'))
        sname = str(request.POST.get('sname'))
        stu_service.add_student(sid, sname)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["POST"])
def update_student(request):
    response = {}
    try:
        sid = int(request.POST.get('sid'))
        sname = str(request.POST.get('sname'))
        stu_service.update_student(sid, sname)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["POST"])
def remove_student(request):
    response = {}
    try:
        sid = int(request.POST.get('sid'))
        stu_service.remove_student(sid)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_student(request):
    response = {}
    try:
        sid = int(request.GET.get('sid'))
        stu = stu_service.find_student(sid)
        response['info'] = {"sid":stu.id,"sname":stu.SNAME}
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["POST"])
def insert_student_info(request):
    response = {}
    try:
        sid = int(request.POST.get('sid'))
        ssex = str(request.POST.get('ssex'))
        smajor = str(request.POST.get('smajor'))
        sintro = str(request.POST.get('sintro'))
        stu_service.add_info(sid, ssex, smajor, sintro)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["POST"])
def update_student_info(request):
    response = {}
    try:
        sid = int(request.POST.get('sid'))
        ssex = str(request.POST.get('ssex'))
        smajor = str(request.POST.get('smajor'))
        sintro = str(request.POST.get('sintro'))
        stu_service.update_info(sid, ssex, smajor, sintro)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_student_info(request):
    response = {}
    try:
        sid = int(request.GET.get('sid'))
        info = stu_service.find_info(sid)
        response['info'] = {"ssex":info.SSEX,"smajor":info.SMAJOR,"sintro":info.SINTRO}
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["POST"])
def remove_student_info(request):
    response = {}
    try:
        sid = int(request.POST.get('sid'))
        stu_service.remove_info(sid)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["POST"])
def invite_student_to_org(request):
    response = {}
    try:
        sid = int(request.POST.get('sid'))
        oid = int(request.POST.get('oid'))
        stu_service.add_stu_to_org(sid, oid)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["POST"])
def remove_student_from_org(request):
    response = {}
    try:
        sid = int(request.POST.get('sid'))
        oid = int(request.POST.get('oid'))
        stu_service.remove_stu_from_org(sid, oid)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_student_in_orgs(request):
    response = {}
    try:
        oid = int(request.GET.get('oid'))
        response['info'] = stu_service.find_students_in_orgs(oid)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_orgs_of_stus(request):
    response = {}
    try:
        sid = int(request.GET.get('sid'))
        response['info'] = stu_service.find_orgs_of_students(sid)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def is_member(request):
    response = {}
    try:
        sid = int(request.GET.get('sid'))
        oid = int(request.GET.get('oid'))
        response['info'] = stu_service.is_member(oid, sid)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def is_charger(request):
    response = {}
    try:
        sid = int(request.GET.get('sid'))
        oid = int(request.GET.get('oid'))
        response['info'] = stu_service.is_charger(oid, sid)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
