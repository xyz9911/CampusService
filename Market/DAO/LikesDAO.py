from .BaseDAO import BaseDAO
from .StudentDAO import *
from .CommodityDAO import *
from ..models import *


class StuStarsDAO(BaseDAO):
    MODEL_CLASS = StuStars
    stuDAO = StudentDAO()
    comDAO = CommodityDAO()

    def add_star(self, sid, cid):
        stu = self.stuDAO.get_student(sid)
        if not stu:
            raise Exception("student not found")
        com = self.comDAO.get_commodity(cid)
        if not com:
            raise Exception("commodity not found")
        star = StuStars()
        star.student=stu
        star.commodity=com
        return self.save(star)

    def remove_star(self, sid, cid):
        stu = self.stuDAO.get_student(sid)
        if not stu:
            raise Exception("student not found")
        com = self.comDAO.get_commodity(cid)
        if not com:
            raise Exception("commodity not found")
        star = StuStars()
        star.student = stu
        star.commodity = com
        return self.delete(star)

    def get_all_stars(self, sid):
        stu = self.stuDAO.get_student(sid)
        if not stu:
            raise Exception("student not found")
        param = {"student": stu}
        res = self.MODEL_CLASS.objects.filter(**param)
        coms = []
        for obj in res:
            coms.append(obj.commodity)
        return coms

    def get_starred(self,cid):
        com = self.comDAO.get_commodity(cid)
        if not com:
            raise Exception("commodity not found")
        param = {"commodity": com}
        return self.find_queryset(param,{},[])

    def get_stars_count(self, cid):
        com = self.comDAO.get_commodity(cid)
        if not com:
            raise Exception("commodity not found")
        param = {"commodity": com}
        return self.get_count(param,{})

    def is_starred(self, sid, cid):
        stu = self.stuDAO.get_student(sid)
        if not stu:
            raise Exception("student not found")
        com = self.comDAO.get_commodity(cid)
        if not com:
            raise Exception("commodity not found")
        param1 = {"student": stu}
        param2 = {"commodity": com}
        return self.is_exists(param1, param2)


class StuLikesDAO(BaseDAO):
    MODEL_CLASS = StuLikes
    stuDAO = StudentDAO()
    comDAO = CommodityDAO()

    def add_like(self, sid, cid):
        stu = self.stuDAO.get_student(sid)
        if not stu:
            raise Exception("student not found")
        com = self.comDAO.get_commodity(cid)
        if not com:
            raise Exception("commodity not found")
        like = StuLikes()
        like.student = stu
        like.commodity = com
        return self.save(like)

    def remove_like(self, sid, cid):
        stu = self.stuDAO.get_student(sid)
        if not stu:
            raise Exception("student not found")
        com = self.comDAO.get_commodity(cid)
        if not com:
            raise Exception("commodity not found")
        like = StuLikes()
        like.student = stu
        like.commodity = com
        return self.delete(like)

    def get_likes_count(self, cid):
        com = self.comDAO.get_commodity(cid)
        param = {"commodity": com}
        return self.get_count(param,{})

    def is_liked(self, sid, cid):
        stu = self.stuDAO.get_student(sid)
        if not stu:
            raise Exception("student not found")
        com = self.comDAO.get_commodity(cid)
        if not com:
            raise Exception("commodity not found")
        param1 = {"student": stu}
        param2 = {"commodity": com}
        return self.is_exists(param1, param2)
