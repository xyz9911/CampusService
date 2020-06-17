from ..DAO.NoticeDAO import *
from django.core.paginator import Paginator


class NoticeService:
    noticeDAO = NoticeDAO()

    def post_notice(self, sid: int, content: str):
        stu = StudentDAO.get_student(sid)
        notice = Notice()
        notice.student = stu
        notice.NCONTENT = content
        return self.noticeDAO.add_notice(notice)

    def delete_notice(self, nid):
        return self.noticeDAO.delete_notice(nid)

    def get_unread_notice(self, sid):
        return self.noticeDAO.get_unread_notice(sid)

    def get_read_notice(self, sid):
        return self.noticeDAO.get_read_notice(sid)

    def get_notice(self, nid):
        return self.noticeDAO.get_notice(nid)

    def read_notice(self, nid):
        return self.noticeDAO.update_notice(nid, True)
