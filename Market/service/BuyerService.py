from ..DAO.StudentDAO import *
from ..DAO.LikesDAO import *
from ..DAO.HistoryDAO import *
from ..DAO.NoticeDAO import *
from django.core.paginator import Paginator


class BuyerService:
    def __init__(self):
        self.stuDAO = StudentDAO()
        self.stuInfoDAO = StudentInfoDAO()
        self.hisDAO = HistoryDAO()
        self.noticeDAO = NoticeDAO()

    def insert_student(self, sid, sname):
        stu = Student()
        stu.id = sid
        stu.SNAME = sname
        if not self.stuDAO.add_student(stu):
            raise Exception("error during insert student")
        else:
            return True

    def get_student(self, sid):
        stu = self.stuDAO.get_student(sid)
        if not stu:
            raise Exception("student not found")
        return stu

    def get_student_info(self, sid):
        info = self.stuInfoDAO.get_info(sid)
        if not info:
            raise Exception("student info not found")
        return info

    def insert_student_info(self, sid, nickname, avatar, sex, major, address, qq, tel):
        stu = self.stuDAO.get_student(sid)
        if not stu:
            raise Exception("student not found")
        info = StudentInfo()
        info.SNICKNAME = nickname
        info.student = stu
        if avatar:
            info.SAVATAR = avatar

        if sex:
            info.SSEX = sex

        if major:
            info.SMAJOR = major

        if address:
            info.SADDRESS = address

        if qq:
            info.SQQ = qq

        if tel:
            info.STEL = tel

        if not self.stuInfoDAO.add_info(info):
            raise Exception("error during inserting student info")
        else:
            return True

    def update_student_info(self, sid, nickname, avatar, sex, major, address, qq, tel):
        info = self.stuInfoDAO.get_info(sid)
        if not info:
            raise Exception("student not found")
        if nickname:
            info.SNICKNAME = nickname

        if avatar:
            info.SAVATAR = avatar

        if sex:
            info.SSEX = sex

        if major:
            info.SMAJOR = major

        if address:
            info.SADDRESS = address

        if qq:
            info.SQQ = qq

        if tel:
            info.STEL = tel

        if not self.stuInfoDAO.update_info(info):
            raise Exception("error during updating student info")

    def get_buyer_history(self, sid):
        stu = self.stuDAO.get_student(sid)
        if not stu:
            raise Exception("student not found")
        result=self.hisDAO.get_buyer_history(sid)
        list=[]
        for obj in result:
            list.append({"cid":obj.commodity.id,"cname":obj.commodity.CNAME,"cprice":obj.commodity.CPRICE,"cimage":obj.commodity.CIMAGE,"hdate":obj.HDATE})
        return list

    def get_unread_notice(self, sid):
        stu = self.stuDAO.get_student(sid)
        if not stu:
            raise Exception("student not found")
        return self.noticeDAO.get_unread_notice(stu)

    def get_read_notice(self, sid):
        stu = self.stuDAO.get_student(sid)
        if not stu:
            raise Exception("student not found")
        return self.noticeDAO.get_read_notice(stu)

    def get_notice(self, nid):
        notice = self.noticeDAO.get_notice(nid)
        if not notice:
            raise Exception("notice not found")
        return notice

    def delete_notice(self, nid):
        notice = self.noticeDAO.get_notice(nid)
        if not notice:
            raise Exception("notice not found")
        return self.noticeDAO.delete_notice(nid)

    def read_notice(self, nid):
        notice = self.noticeDAO.get_notice(nid)
        if not notice:
            raise Exception("notice not found")
        return self.noticeDAO.update_notice(nid, True)
