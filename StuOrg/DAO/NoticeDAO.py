from .BaseDAO import BaseDAO
from ..models import *
from .StudentDAO import *


class NoticeDAO(BaseDAO):
    MODEL_CLASS = Notice

    def __init__(self):
        self.orgDAO = OrgDAO()

    def add_notice(self, oid, ncontent):
        org = self.orgDAO.find_org(oid)
        notice = Notice(organization=org, NCONTENT=ncontent)
        self.save(notice)
        return notice.id

    def find_notice(self, nid):
        param = {"id": nid}
        return self.find_one(param, {}, [])

    def remove_notice(self, nid):
        notice = self.find_notice(nid)
        return self.delete(notice)

    def update_notice(self, nid, ncontent):
        notice = self.find_notice(nid)
        notice.NCONTENT = ncontent
        return self.update(notice)

    def find_notice_by_org(self, oid):
        org = self.orgDAO.find_org(oid)
        param = {"organization": org}
        res = self.find_queryset(param, {}, [])
        notices = []
        for obj in res:
            notices.append({"nid": obj.id, "ncontent": obj.NCONTENT, "ntime": obj.NTIME})
        return notices


class NoticeStuDAO(BaseDAO):
    MODEL_CLASS = NoticeStu

    def __init__(self):
        self.noticeDAO = NoticeDAO()
        self.stuDAO = StudentDAO()

    def add_relation(self, sid, nid):
        stu = self.stuDAO.find_student(sid)
        notice = self.noticeDAO.find_notice(nid)
        relation = NoticeStu(notice=Notice, student=Student)
        return self.save(relation)

    def find_relation(self, sid, nid):
        stu = self.stuDAO.find_student(sid)
        notice = self.noticeDAO.find_notice(nid)
        param = {"student": stu, "notice": notice}
        return self.find_one(param, {}, [])

    def update_relation(self, sid, nid):
        relation = self.find_relation(sid, nid)
        relation.NISREAD = True
        return self.update(relation)

    def find_notice_by_stu(self, sid, status):
        stu = self.stuDAO.find_student(sid)
        param = {"student": stu, "NISREAD": status}
        res = self.find_queryset(param, {}, [])
        notices = []
        for obj in res:
            org = obj.organization
            notices.append({"nid": obj.id, "oid": org.id, "oname": org.ONAME, "oimage": org.OIMAGE, "ntime": obj.NTIME})
        return notices

    def add_relation_batch(self, relations):
        return self.save_batch(relations)
