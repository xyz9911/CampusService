from ..DAO.StudentDAO import *
from ..DAO.LikesDAO import *
from ..DAO.HistoryDAO import *
from ..DAO.NoticeDAO import *
from django.core.paginator import Paginator


class CommodityService:
    def __init__(self):
        self.stuDAO = StudentDAO()
        self.stuInfoDAO = StudentInfoDAO()
        self.starDAO = StuStarsDAO()
        self.likeDAO = StuLikesDAO()
        self.comDAO = CommodityDAO()
        self.comInfoDAO = CommodityInfoDAO()
        self.hisDAO = HistoryDAO()
        self.ratingDAO = RatingDAO()

    def star_or_unstar_commodity(self, sid, cid, star_or_unstar):
        if star_or_unstar:
            return self.starDAO.add_star(sid, cid)

        else:
            return self.starDAO.remove_star(sid, cid)

    def get_starred_commodity(self, sid):
        return self.starDAO.get_all_stars(sid)

    def check_star_status(self, sid, cid):
        return self.starDAO.is_starred(sid, cid)

    def like_or_unlike_commodity(self, sid, cid, like_or_unlike):
        if like_or_unlike:
            return self.likeDAO.add_like(sid, cid)

        else:
            return self.likeDAO.remove_like(sid, cid)

    def check_like_status(self, sid, cid):
        return self.likeDAO.is_liked(sid, cid)

    def view_commodities(self, pindex):
        commodity_list = self.comDAO.get_commodities_view()
        paginator = Paginator(commodity_list, 10)
        if pindex == "":  # django中默认返回空值，所以加以判断，并设置默认值为1
            pindex = 1
        else:  # 如果有返回在值，把返回值转为整数型
            int(pindex)

        return paginator.page(pindex)

    def view_commodity_info(self, cid):
        com = self.comDAO.get_commodity(cid)
        if not com:
            raise Exception("commodity not found")
        info = self.comInfoDAO.get_info(cid)
        quantity=0;des=""
        found=False
        if info:
            quantity=info.CQUANTITY
            des=info.CDESCRIPTION
            found=True
        stu_info = self.stuInfoDAO.get_info(com.student.id)
        stars = self.starDAO.get_stars_count(cid)
        likes = self.likeDAO.get_likes_count(cid)
        return {"cid": com.id, "snickname": stu_info.SNICKNAME, "savatar": stu_info.SAVATAR,
                "saddress": stu_info.SADDRESS, "srating": stu_info.SRATING,
                "sqq": stu_info.SQQ, "stel": stu_info.STEL,
                "cname": com.CNAME, "cimage": com.CIMAGE, "cprice": com.CPRICE, "cdate": com.CDATE,
                "cquantity": quantity, "cdescription": des,
                "clikes": likes, "stars": stars, "liked": self.check_like_status(com.student.id, cid),
                "stared": self.check_star_status(com.student.id, cid),"infoadded":found}

    def rate_commodity(self, sid, cid, rating):
        if not self.hisDAO.get_history_by_stu_and_com(sid, cid):
            raise Exception("no history found")

        else:
            stu = self.stuDAO.get_student(sid)
            com = self.comDAO.get_commodity(cid)
            rate = Rating
            rate.student = stu
            rate.commodity = com
            rate.RATING = rating
            return self.ratingDAO.add_rating(rate)
