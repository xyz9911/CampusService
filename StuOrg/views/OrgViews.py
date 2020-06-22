from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json
from ..service.OrgService import *

org_service = OrgService()


@require_http_methods(["POST"])
def post_org(request):
    response = {}
    try:
        oname = str(request.POST.get('oname'))
        oimage = str(request.POST.get('oimage'))
        odes = str(request.POST.get('odes'))
        org_service.add_org(oname, oimage, odes)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["POST"])
def update_org(request):
    response = {}
    try:
        oid = int(request.POST.get('oid'))
        oname = int(request.POST.get('oname'))
        oimage = str(request.POST.get('oimage'))
        odes = str(request.POST.get('odes'))
        org_service.update_org(oid, oname, oimage, odes)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["POST"])
def remove_org(request):
    response = {}
    try:
        oid = int(request.POST.get('oid'))
        org_service.remove_org(oid)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_org(request):
    response = {}
    try:
        oid = int(request.GET.get('oid'))
        org = org_service.find_org(oid)
        response['info'] = json.loads(serializers.serialize("json", org))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_all_orgs(request):
    response = {}
    try:
        res = org_service.find_all_orgs()
        response['info'] = json.loads(serializers.serialize("json", res))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["POST"])
def add_stu_as_charge(request):
    response = {}
    try:
        oid = int(request.POST.get('oid'))
        sid = str(request.POST.get('sid'))
        sduty = str(request.POST.get('sduty'))
        org_service.add_stu_as_charge(oid, sid, sduty)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["POST"])
def remove_stu_as_charge(request):
    response = {}
    try:
        oid = int(request.POST.get('oid'))
        sid = str(request.POST.get('sid'))
        org_service.remove_stu_charge(oid, sid)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["POST"])
def update_stu_charge(request):
    response = {}
    try:
        oid = int(request.POST.get('oid'))
        sid = str(request.POST.get('sid'))
        sduty = str(request.POST.get('sduty'))
        org_service.update_charge(oid, sid, sduty)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_orgs_by_stu(request):
    response = {}
    try:
        sid = int(request.GET.get('sid'))
        response['info'] = org_service.find_org_by_stu(sid)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_orgs_charges(request):
    response = {}
    try:
        oid = int(request.GET.get('oid'))
        response['info'] = org_service.find_charge_by_org(oid)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
