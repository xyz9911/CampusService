from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .models import *


@require_http_methods(["POST"])
def stu_login(request):
    response = {}
    try:
        sid = int(request.POST.get('sid'))
        spassword = str(request.POST.get('spassword'))
        stu = Student.objects.get(id=sid)
        if stu.SPASSWORD == spassword and stu.SISVALID is True:
            response['info'] = {"sid": sid, "sname": stu.SNAME, "code": 200}
        else:
            response['info'] = {"code": 100}
        # response['info'] = json.loads(serializers.serialize("json", info))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['info'] = {"code": 100}
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["POST"])
def stu_ban(request):
    response = {}
    try:
        sid = int(request.POST.get('sid'))
        stu = Student.objects.get(id=sid)
        stu.SISVALID = False
        stu.save(stu)
        # response['info'] = json.loads(serializers.serialize("json", info))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["POST"])
def admin_login(request):
    response = {}
    try:
        aid = int(request.POST.get('aid'))
        apassword = str(request.POST.get('apassword'))
        admin = Admin.objects.get(id=aid)
        if admin.APASSWORD == apassword:
            response['info'] = {"aid": aid, "code": 200}
        else:
            response['info'] = {"code": 100}
        # response['info'] = json.loads(serializers.serialize("json", info))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['info'] = {"code": 100}
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
