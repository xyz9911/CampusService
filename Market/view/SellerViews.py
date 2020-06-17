from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json
from ..service.SellerService import *
from ..models import *

seller_service = SellerService()


@require_http_methods(["POST"])
def post_commodity(request):
    response = {}
    try:
        sid = int(request.POST.get('sid'))
        cname = str(request.POST.get('cname'))
        cimage = str(request.POST.get('cimage'))
        cprice = float(request.POST.get('cprice'))
        seller_service.post_commodity(sid, cname, cimage, cprice)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["POST"])
def post_commodity_info(request):
    response = {}
    try:
        cid = int(request.POST.get('cid'))
        quantity = str(request.POST.get('quantity'))
        description = str(request.POST.get('description'))
        seller_service.post_commodity_info(cid, quantity, description)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["POST"])
def update_commodity(request):
    response = {}
    try:
        cid = int(request.POST.get('cid'))
        cname = str(request.POST.get('cname'))
        cimage = str(request.POST.get('cimage'))
        cprice = float(request.POST.get('cprice'))
        seller_service.update_commodity(cid, cname, cimage, cprice)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["POST"])
def update_commodity_info(request):
    response = {}
    try:
        cid = int(request.POST.get('cid'))
        quantity = int(request.POST.get('quantity'))
        description = str(request.POST.get('description'))
        seller_service.update_commodity_info(cid, quantity, description)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["POST"])
def confirm_transaction(request):
    response = {}
    try:
        cid = int(request.POST.get('cid'))
        sid = int(request.POST.get('sid'))
        seller_service.confirm_transaction(cid, sid)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_selling_commodities(request):
    response = {}
    try:
        sid = int(request.GET.get('sid'))
        coms = seller_service.get_selling_commodities(sid)
        response['info'] = json.loads(serializers.serialize("json", coms))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["POST"])
def post_notice(request):
    response = {}
    try:
        sid = int(request.POST.get('sid'))
        ncontent = str(request.POST.get('ncontent'))
        seller_service.insert_notice(sid, ncontent)
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_sold_commodities(request):
    response = {}
    try:
        sid = int(request.GET.get('sid'))
        coms = seller_service.get_sold_commodities(sid)
        response['info'] = json.loads(serializers.serialize("json", coms))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
