from ..DAO.OrgDAO import *


class StudentService:
    def __init__(self):
        self.stuDAO = StudentDAO()
        self.stuInfoDAO = StudentInfoDAO()
        self.stuOrgDAO = StuOrgDAO()
        self.orgChargeDAO = OrgChargeDAO()

    def add_student(self, sid, sname):
        if not self.stuDAO.add_student(sid, sname):
            raise Exception("insert error")
        return True

    def update_student(self, sid, sname):
        if not self.stuDAO.update_student(sid, sname):
            raise Exception("update error")
        return True

    def remove_student(self, sid):
        if not self.stuDAO.remove_student(sid):
            raise Exception("remove error")
        return True

    def find_student(self, sid):
        return self.stuDAO.find_student(sid)

    def add_info(self, sid, ssex, smajor, sintro):
        if not self.stuInfoDAO.add_info(sid, ssex, smajor, sintro):
            raise Exception("insert error")
        return True

    def update_info(self, sid, ssex, smajor, sintro):
        if not self.stuInfoDAO.update_info(sid, ssex, smajor, sintro):
            raise Exception("update error")
        return True

    def find_info(self, sid):
        return self.stuInfoDAO.find_info(sid)

    def remove_info(self, sid):
        if not self.stuInfoDAO.remove_info(sid):
            raise Exception("remove error")
        return True

    def add_stu_to_org(self, sid, oid):
        if not self.stuOrgDAO.add_relation(sid, oid):
            raise Exception("insert error")
        return True

    def remove_stu_from_org(self, sid, oid):
        if not self.stuOrgDAO.remove_relation(sid, oid):
            raise Exception("remove error")
        return True

    def find_students_in_orgs(self, oid):
        return self.stuOrgDAO.find_students(oid)

    def find_orgs_of_students(self, sid):
        return self.stuOrgDAO.find_orgs(sid)

    def is_member(self, oid, sid):
        return self.stuOrgDAO.stu_exists(oid, sid)

    def is_charger(self, oid, sid):
        return self.orgChargeDAO.stu_exists(oid, sid)
