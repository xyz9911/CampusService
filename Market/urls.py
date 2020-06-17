from django.conf.urls import url, include
from Market.view import BuyerViews
from Market.view import SellerViews
from Market.view import CommodityViews

urlpatterns = [
    url(r'^show_student$', BuyerViews.show_student),
    url(r'^show_stu_info$', BuyerViews.show_student_info),
    url(r'^insert_student$', BuyerViews.insert_student),
    url(r'^insert_student_info$', BuyerViews.insert_student_info),
    url(r'^update_student_info$', BuyerViews.update_student_info),
    url(r'^show_buyer_history$', BuyerViews.show_buyer_history),
    url(r'^show_unread_notices$', BuyerViews.show_unread_notices),
    url(r'^show_read_notices$', BuyerViews.show_read_notices),
    url(r'^show_notice$', BuyerViews.show_notice),
    url(r'^read_notice$', BuyerViews.read_notice),

    url(r'^star_commodity$', CommodityViews.star_commodity),
    url(r'^star_commodity$', CommodityViews.star_commodity),
    url(r'^unstar_commodity$', CommodityViews.unstar_commodity),
    url(r'^show_starred_commodity$', CommodityViews.show_starred_commodity),
    url(r'^check_starred_status$', CommodityViews.check_starred_status),
    url(r'^show_all_commodities$', CommodityViews.show_all_commodities),
    url(r'^show_commodity_info$', CommodityViews.show_commodity_info),

    url(r'^post_commodity$', SellerViews.post_commodity),
    url(r'^post_commodity_info$', SellerViews.post_commodity_info),
    url(r'^update_commodity$', SellerViews.update_commodity),
    url(r'^update_commodity_info$', SellerViews.update_commodity_info),
    url(r'^confirm_transaction$', SellerViews.confirm_transaction),
    url(r'^show_selling_commodities$', SellerViews.show_selling_commodities),
    url(r'^show_sold_commodities$', SellerViews.show_sold_commodities),
    url(r'^post_notice$', SellerViews.post_notice),
]
