from .StudentDAO import *
from .CommodityDAO import *
from ..models import *


class HistoryDAO(BaseDAO):
    MODEL_CLASS = History
    stuDAO = StudentDAO()
    comDAO = CommodityDAO()

    def add_history(self, his):
        return self.save(his)

    def get_buyer_history(self, buyer_id):
        stu = self.stuDAO.get_student(buyer_id)
        param = {"buyer": stu}
        order = ["HDATE"]
        return self.find_queryset(param, {}, order)

    def get_seller_history(self, seller_id):
        stu = self.stuDAO.get_student(seller_id)

        param = {"seller": stu}
        order = ["HDATE"]
        return self.find_queryset(param, {}, order)

    def get_history(self, hid):
        param = {"id": hid}
        return self.find_one(param)

    def get_history_by_stu_and_com(self, sid, cid):
        stu = self.stuDAO.get_student(sid)
        com = self.comDAO.get_commodity(cid)
        param = {"student": stu, "commodity": com}
        return self.is_exists(param)
