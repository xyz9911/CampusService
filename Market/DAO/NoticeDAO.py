from .BaseDAO import BaseDAO
from .StudentDAO import StudentDAO
from ..models import *


class NoticeDAO(BaseDAO):
    MODEL_CLASS = Notice

    def get_unread_notice(self, student):
        param = {"student": student, "NISREAD": False}
        order = ["NDATE"]
        return self.find_queryset(param, {}, order)

    def add_notice(self, notice):
        return self.save(notice)

    def add_notices(self, notices):
        return self.save_batch(notices)

    def get_read_notice(self, student):
        param = {"student": student, "NISREAD": True}
        order = ["NDATE"]
        return self.find_queryset(param, {}, order)

    def delete_notice(self, nid: int):
        param = {"id": nid}
        res = self.find_queryset(param)
        return self.delete(res)

    def get_notice(self, nid: int):
        param = {"id": nid}
        return self.find_one(param,{},[])

    def update_notice(self, nid, isread):
        param = {"id": nid}
        notice = self.find_one(param,{},[])
        notice.NISREAD = isread
        return self.update(notice)
