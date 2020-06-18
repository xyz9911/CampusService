from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json
from ..service.CommodityService import *
from ..service.BuyerService import *
from ..models import *

com_service = CommodityService()
buyer_service=BuyerService()


@require_http_methods(["POST"])
def star_commodity(request):
    response = {}
    try:
        sid = int(request.POST.get('sid'))
        cid = int(request.POST.get('cid'))
        com_service.star_or_unstar_commodity(sid, cid, True)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["POST"])
def unstar_commodity(request):
    response = {}
    try:
        sid = int(request.POST.get('sid'))
        cid = int(request.POST.get('cid'))
        com_service.star_or_unstar_commodity(sid, cid, False)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_starred_commodity(request):
    response = {}
    try:
        sid = int(request.GET.get('sid'))
        coms = com_service.get_starred_commodity(sid)
        res=[]
        for obj in coms:
            stu_info = obj.student.studentinfo
            res.append(
                {"cid":obj.id,"snickname": stu_info.SNICKNAME, "savatar": stu_info.SAVATAR, "cname": obj.CNAME,
                 "cimage": obj.CIMAGE, "cprice": obj.CPRICE, "cdate": obj.CDATE})
        response['info'] = res
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def check_starred_status(request):
    response = {}
    try:
        sid = int(request.GET.get('sid'))
        cid = int(request.GET.get('cid'))
        status = com_service.check_star_status(sid, cid)
        # response['info'] = {"sid": sid, "saddress": info.SADDRESS, "savatar": info.SAVATAR, "smajor": info.SNICKNAME,
        #                     "srating": info.SRATING, "ssex": info.SSEX}
        response['info'] = status
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["POST"])
def like_commodity(request):
    response = {}
    try:
        sid = int(request.POST.get('sid'))
        cid = int(request.POST.get('cid'))
        com_service.like_or_unlike_commodity(sid, cid, True)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["POST"])
def unlike_commodity(request):
    response = {}
    try:
        sid = int(request.POST.get('sid'))
        cid = int(request.POST.get('cid'))
        com_service.like_or_unlike_commodity(sid, cid, False)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def check_liked_status(request):
    response = {}
    try:
        sid = int(request.GET.get('sid'))
        cid = int(request.GET.get('cid'))
        status = com_service.check_like_status(sid, cid)
        response['info'] = status
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_all_commodities(request):
    response = {}
    try:
        pindex = int(request.GET.get('pindex'))
        coms = com_service.view_commodities(pindex)
        coms_page = []
        res = coms.object_list
        for obj in res:
            stu_info = obj.student.studentinfo
            coms_page.append(
                {"cid":obj.id,"snickname": stu_info.SNICKNAME, "savatar": stu_info.SAVATAR, "cname": obj.CNAME,
                 "cimage": obj.CIMAGE, "cprice": obj.CPRICE, "cdate": obj.CDATE})
        response['pageInfo']={"current_page": coms.number, "all_pages": coms.paginator.num_pages, "count": coms.paginator.count}
        response['info'] = coms_page
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_commodity_info(request):
    response = {}
    try:
        cid = int(request.GET.get('cid'))
        info = com_service.view_commodity_info(cid)
        response['info'] = info
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["POST"])
def rate_commodity(request):
    response = {}
    try:
        sid = int(request.POST.get('sid'))
        cid = int(request.POST.get('cid'))
        rating = int(request.POST.get("rating"))
        com_service.rate_commodity(sid, cid, rating)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)