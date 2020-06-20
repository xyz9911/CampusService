from .BaseDAO import BaseDAO
from ..models import *
from .StudentDAO import *


class OrgDAO(BaseDAO):
    MODEL_CLASS = Organization

    def add_org(self, oname, oimage, odes):
        org = Organization(ONAME=oname, OIMAGE=oimage, ODESCRIPTION=odes)
        return self.save(org)

    def find_org(self, oid):
        param = {"id": oid}
        return self.find_one(param)

    def remove_org(self, oid):
        org = self.find_org(oid)
        return self.delete(org)

    def find_all_orgs(self):
        return self.find_queryset({}, {}, [])

    def update_org(self, oid, oname, oimage, odes):
        org = self.find_org(oid)
        org.ONAME = oname
        org.OIMAGE = oimage
        org.ODES = odes
        return self.update(org)


class OrgChargeDAO(BaseDAO):
    MODEL_CLASS = OrgCharge

    def __init__(self):
        self.stuDAO = StudentDAO()
        self.orgDAO = OrgDAO()

    def add_charge(self, oid, sid, sduty):
        org = self.orgDAO.find_org(oid)
        stu = self.stuDAO.find_student(sid)
        charge = OrgCharge(organization=org, student=stu, SDUTY=sduty)
        return self.save(charge)

    def find_charge(self, oid, sid):
        org = self.orgDAO.find_org(oid)
        stu = self.stuDAO.find_student(sid)
        param = {"organization": org, "student": stu}
        return self.find_one(param, {}, [])

    def remove_charge(self, oid, sid):
        charge = self.find_charge(oid, sid)
        return self.delete(charge)

    def update_charge(self, oid, sid, sduty):
        charge = self.find_charge(oid, sid)
        charge.SDUTY = sduty
        return self.update(charge)

    def find_charge_by_org(self, oid):
        org = self.orgDAO.find_org(oid)
        param = {"organization": org}
        res = self.find_queryset(param, {}, [])
        students = []
        for obj in res:
            stu = obj.student
            info = stu.studentinfo
            students.append(
                {"sid": stu.id, "sname": stu.SNAME, "sduty": obj.SDUTY, "otime": obj.OTIME, "ssex": info.SSEX,
                 "smajor": info.SMAJOR, "sintro": info.SINTRO})
        return students

    def find_charge_by_org_raw(self, oid):
        org = self.orgDAO.find_org(oid)
        param = {"organization": org}
        res = self.find_queryset(param, {}, [])
        students = []
        for obj in res:
            stu = obj.student
            students.append(stu)
        return students

    def stu_exists(self, oid, sid):
        stu = self.stuDAO.find_student(sid)
        org = self.orgDAO.find_org(oid)
        param = {"student": stu, "organization": org}
        return self.is_exists(param, {}, [])


class StuOrgDAO(BaseDAO):
    MODEL_CLASS = OrgStu

    def __init__(self):
        self.stuDAO = StudentDAO()
        self.orgDAO = OrgDAO()

    def find_relation(self, sid, oid):
        stu = self.stuDAO.find_student(sid)
        if not stu:
            raise Exception("student not found")
        org = self.orgDAO.find_org(oid)
        if not org:
            raise Exception("org not found")
        param = {"student": stu, "organization": org}
        return self.find_one(param, {}, [])

    def add_relation(self, sid, oid):
        stu = self.stuDAO.find_student(sid)
        if not stu:
            raise Exception("student not found")
        org = self.orgDAO.find_org(oid)
        if not org:
            raise Exception("org not found")
        org_stu = OrgStu(student=stu, organization=org)
        return self.save(org_stu)

    def remove_relation(self, sid, oid):
        org_stu = self.find_relation(sid, oid)
        return self.delete(org_stu)

    def find_students(self, oid):
        org = self.orgDAO.find_org(oid)
        if not org:
            raise Exception("org not found")
        param = {"organization": org}
        relations = self.find_queryset(param, {}, [])
        students = []
        for obj in relations:
            stu = obj.student
            info = stu.studentinfo
            students.append(
                {"sid": stu.id, "sname": stu.SNAME, "ssex": info.SSEX, "smajor": info.SMAJOR, "sintro": info.SINTRO})
        return students

    def find_students_raw(self, oid):
        org = self.orgDAO.find_org(oid)
        if not org:
            raise Exception("org not found")
        param = {"organization": org}
        relations = self.find_queryset(param, {}, [])
        students = []
        for obj in relations:
            stu = obj.student
            students.append(stu)
        return students

    def find_orgs(self, sid):
        stu = self.stuDAO.find_student(sid)
        if not stu:
            raise Exception("student not found")
        param = {"student": stu}
        relations = self.find_queryset(param, {}, [])
        orgs = []
        for obj in relations:
            org = obj.organization
            orgs.append({"oid": org.id, "oname": org.ONAME, "oimage": org.OIMAGE, "odescription": org.ODESCRIPTION})
        return orgs

    def add_batch(self, relations):
        return self.save_batch(relations)

    def stu_exists(self, oid, sid):
        stu = self.stuDAO.find_student(sid)
        org = self.orgDAO.find_org(oid)
        param = {"student": stu, "organization": org}
        return self.is_exists(param, {}, [])
