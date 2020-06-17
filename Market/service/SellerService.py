from ..DAO.StudentDAO import *
from ..DAO.CommodityDAO import *
from ..DAO.HistoryDAO import *


class SellerService:
    stuDAO = StudentDAO()
    comDAO = CommodityDAO()
    infoDAO = CommodityInfoDAO()
    historyDAO = HistoryDAO()

    def post_commodity(self, sid, name, image, price):
        com = Commodity()
        stu = self.stuDAO.get_student(sid)
        com.student = stu
        com.CNAME = name
        com.CIMAGE = image
        com.CPRICE = price
        return self.comDAO.add_commodity(com)

    def post_commodity_info(self, cid, quantity, description):
        info = CommodityInfo()
        com = self.comDAO.get_commodity(cid)
        info.commodity = com
        info.CQUANTITY = quantity
        info.CDESCRIPTION = description
        return self.infoDAO.add_info(info)

    def update_commodity(self, cid, name, image, price):
        com = self.comDAO.get_commodity(cid)
        if not com:
            raise Exception("commodity not found")
        if name:
            com.CNAME = name
            com.CIMAGE = image
            com.CPRICE = price

        return self.comDAO.update_commodity(com)

    def update_commodity_info(self, cid, quantity, description):
        info = self.infoDAO.get_info(cid)
        if not info:
            raise Exception("commodity info not found")
        if quantity:
            info.CQUANTITY = quantity
            info.CDESCRIPTION = description

        return CommodityInfoDAO.update_info(info)

    def get_selling_commodities(self, sid):
        stu = self.stuDAO.get_student(sid)
        if not stu:
            raise Exception("student not found")
        return self.comDAO.get_commodities_by_seller(sid, False)

    def get_sold_commodities(self, sid):
        stu = self.stuDAO.get_student(sid)
        if not stu:
            raise Exception("student not found")
        return self.comDAO.get_commodities_by_seller(sid, True)

    def confirm_transaction(self, cid, sid):
        stu = self.stuDAO.get_student(sid)
        if not stu:
            raise Exception("student not found")
        com = self.comDAO.get_commodity(cid)
        if not com:
            raise Exception("commodity not found")
        com.CISSOLD = True
        self.comDAO.update_commodity(com)
        his = History()
        his.commodity = com
        his.buyer = stu
        return self.historyDAO.add_history(his)
