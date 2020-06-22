from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json
from ..service.BuyerService import *
from ..models import *

buyer_service = BuyerService()


@require_http_methods(["GET"])
def show_student(request):
    response = {}
    try:
        sid = int(request.GET.get('sid'))
        stu = buyer_service.get_student(sid)
        response['info'] = {"sid": sid, "sname": stu.SNAME}
        # response['info'] = json.loads(serializers.serialize("json", info))
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
        info = buyer_service.get_student_info(sid)
        response['info'] = {"sid": sid,"snickname":info.SNICKNAME, "saddress": info.SADDRESS, "savatar": info.SAVATAR, "smajor": info.SMAJOR,
                            "srating": info.SRATING, "ssex": info.SSEX, "sqq": info.SQQ, "stel": info.STEL}
        # response['info'] = json.loads(serializers.serialize("json", info))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["POST"])
def insert_student(request):
    response = {}
    try:
        sid = int(request.POST.get('sid'))
        sname = str(request.POST.get('sname'))
        buyer_service.insert_student(sid, sname)
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
        snickname = str(request.POST.get('snickname'))
        savatar = str(request.POST.get('savatar'))
        ssex = bool(request.POST.get('ssex'))
        smajor = str(request.POST.get('smajor'))
        saddress = str(request.POST.get('saddress'))
        sqq = str(request.POST.get('sqq'))
        stel = str(request.POST.get('stel'))
        buyer_service.insert_student_info(sid, snickname, savatar, ssex, smajor, saddress, sqq, stel)
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
        snickname = str(request.POST.get('snickname'))
        savatar = str(request.POST.get('savatar'))
        ssex = bool(request.POST.get('ssex'))
        smajor = str(request.POST.get('smajor'))
        saddress = str(request.POST.get('saddress'))
        sqq = str(request.POST.get('sqq'))
        stel = str(request.POST.get('stel'))
        buyer_service.update_student_info(sid, snickname, savatar, ssex, smajor, saddress,sqq,stel)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_buyer_history(request):
    response = {}
    try:
        sid = int(request.GET.get('sid'))
        history = buyer_service.get_buyer_history(sid)
        response['info'] = history
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_unread_notices(request):
    response = {}
    try:
        sid = int(request.GET.get('sid'))
        notices = buyer_service.get_unread_notice(sid)
        response['info'] = json.loads(serializers.serialize("json", notices))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_read_notices(request):
    response = {}
    try:
        sid = int(request.GET.get('sid'))
        notices = buyer_service.get_read_notice(sid)
        response['info'] = json.loads(serializers.serialize("json", notices))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_notice(request):
    response = {}
    try:
        nid = int(request.GET.get('nid'))
        notice = buyer_service.get_notice(nid)
        response['info'] = {"nid":nid,"ncontent":notice.NCONTENT,"ndate":notice.NDATE}
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["POST"])
def read_notice(request):
    response = {}
    try:
        nid = int(request.POST.get('nid'))
        buyer_service.read_notice(nid)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
