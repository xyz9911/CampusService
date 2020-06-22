from ..DAO.NoticeDAO import *
from ..DAO.OrgDAO import *


class NoticeService:
    def __init__(self):
        self.noticeDAO = NoticeDAO()
        self.noticeStuDAO = NoticeStuDAO()
        self.stuOrgDAO = StuOrgDAO()
        self.orgChargeDAO = OrgChargeDAO()
        self.orgDAO = OrgDAO()

    def add_notice(self, oid, ncontent):
        org = self.orgDAO.find_org(oid)
        students = self.stuOrgDAO.find_students_raw(oid)
        chargers = self.orgChargeDAO.find_charge_by_org_raw(oid)
        notice = self.noticeDAO.add_notice(oid, ncontent)
        relations = []
        for obj in students:
            notice_stu = NoticeStu(notice=notice,student=obj)
            relations.append(notice_stu)
        for obj in chargers:
            notice_stu = NoticeStu(notice=notice,student=obj)
            relations.append(notice_stu)
        if not self.noticeStuDAO.add_relation_batch(relations):
            raise Exception("input error")
        return True

    def find_notice(self, nid):
        return self.noticeDAO.find_notice(nid)

    def remove_notice(self, nid):
        if not self.noticeDAO.remove_notice(nid):
            raise Exception("delete error")
        return True

    def update_notice(self, nid, ncontent):
        if not self.noticeDAO.update_notice(nid, ncontent):
            raise Exception("update error")
        return True

    def find_notice_by_org(self, oid):
        return self.noticeDAO.find_notice_by_org(oid)

    def read_notice(self,sid,nid):
        if not self.noticeStuDAO.update_relation(sid,nid):
            raise Exception("update error")
        return True

    def find_unread_notice(self,sid):
        return self.noticeStuDAO.find_notice_by_stu(sid,False)

    def find_read_notice(self,sid):
        return self.noticeStuDAO.find_notice_by_stu(sid,True)
