from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json
from ..service.NoticeService import *

notice_service = NoticeService()


@require_http_methods(["POST"])
def post_notice(request):
    response = {}
    try:
        oid = int(request.POST.get('oid'))
        ncontent = str(request.POST.get('ncontent'))
        notice_service.add_notice(oid, ncontent)
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
        notice = notice_service.find_notice(nid)
        response['info'] = {"nid":notice.id,"ncontent":notice.NCONTENT,"ntime":notice.NTIME}
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["POST"])
def remove_notice(request):
    response = {}
    try:
        nid = int(request.POST.get('nid'))
        notice_service.remove_notice(nid)
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
        sid = int(request.POST.get('sid'))
        nid = int(request.POST.get('nid'))
        notice_service.read_notice(sid, nid)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_notice_by_org(request):
    response = {}
    try:
        oid = int(request.GET.get('oid'))
        notices = notice_service.find_notice_by_org(oid)
        response['info'] = notices
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_unread_notice(request):
    response = {}
    try:
        sid = int(request.GET.get('sid'))
        notices = notice_service.find_unread_notice(sid)
        response['info'] = notices
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_read_notice(request):
    response = {}
    try:
        sid = int(request.GET.get('sid'))
        notices = notice_service.find_read_notice(sid)
        response['info'] = notices
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
