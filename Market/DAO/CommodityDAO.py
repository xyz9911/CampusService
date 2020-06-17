from .BaseDAO import BaseDAO
from .StudentDAO import *
from ..models import *


class CommodityDAO(BaseDAO):
    MODEL_CLASS = Commodity
    stuDAO = StudentDAO()

    def add_commodity(self, com):
        return self.save(com)

    def update_commodity(self, com):
        return self.update(com)

    def get_commodity(self, cid):
        param = {"id": cid}
        return self.find_one(param, {}, [])

    def get_commodities(self):
        param = {"CISSOLD": True, "is_delete": True}
        order = ["CDATE"]
        return self.find_queryset({}, param, order)

    def get_commodities_view(self):
        param = {"CISSOLD": True, "is_delete": True}
        order = ["CDATE"]
        res = self.MODEL_CLASS.objects.filter().exclude(**param).order_by(*order)
        return res

    def get_commodities_by_seller(self, sid,cissold):
        stu = self.stuDAO.get_student(sid)
        param1 = {"student": stu,"CISSOLD":cissold}
        param2 = {"is_delete": True}
        return self.find_queryset(param1, param2)


class CommodityInfoDAO(BaseDAO):
    MODEL_CLASS = CommodityInfo
    comDAO = CommodityDAO()

    def add_info(self, info):
        return self.save(info)

    def update_info(self, info):
        return self.update(info)

    def get_info(self, cid):
        com = self.comDAO.get_commodity(cid)
        param = {"commodity": com}
        return self.find_one(param, {},[])


class RatingDAO(BaseDAO):
    MODEL_CLASS = Rating
    stuDAO = StudentDAO()
    comDAO = CommodityDAO()

    def add_rating(self, rating):
        return self.save(rating)

    def delete_rating(self, rid):
        param = {id: rid}
        res = self.find_one(param)
        return self.delete(res)

    def get_rating(self, rid):
        param = {id: rid}
        return self.find_one(param)

    def get_ratings(self, sid):
        stu = self.stuDAO.get_student(sid)
        param = {"student": stu}
        return self.find_queryset(param)

    def get_rating_by_com(self, cid):
        com = self.comDAO.get_commodity(cid)
        param = {"commodity": com}
        return self.find_one(param)
