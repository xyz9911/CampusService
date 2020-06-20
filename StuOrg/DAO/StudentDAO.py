from .OrgDAO import *
from ..models import *


class StudentDAO(BaseDAO):
    MODEL_CLASS = Student

    def add_student(self, sid, sname):
        stu = Student(id=sid, SNAME=sname)
        return self.save(stu)

    def update_student(self, sid, sname):
        stu = self.find_student(sid)
        if not stu:
            raise Exception("student not found")
        stu.SNAME = sname
        return self.update(stu)

    def remove_student(self, sid):
        stu = self.find_student(sid)
        if not stu:
            raise Exception("student not found")
        return self.delete(stu)

    def find_student(self, sid):
        param = {"id": sid}
        return self.find_one(param, {}, [])


class StudentInfoDAO(BaseDAO):
    MODEL_CLASS = StudentInfo

    def __init__(self):
        self.stuDAO = StudentDAO()

    def add_info(self, sid, ssex, smajor, sintro):
        stu = self.stuDAO.find_student(sid)
        info = StudentInfo(student=stu, SSEX=ssex, SMAJOR=smajor, SINTRO=sintro)
        return self.save(info)

    def update_info(self, sid, ssex, smajor, sintro):
        stu = self.stuDAO.find_student(sid)
        if not stu:
            raise Exception("student not found")
        info = StudentInfo(student=stu, SSEX=ssex, SMAJOR=smajor, SINTRO=sintro)
        return self.save(info)

    def find_info(self, sid):
        stu = self.stuDAO.find_student(sid)
        if not stu:
            raise Exception("student not found")
        param = {"student": stu}
        return self.find_one(param, {}, [])

    def remove_info(self, sid):
        info = self.find_info(sid)
        return self.delete(info)


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

    def stu_exists(self,oid,sid):
        stu = self.stuDAO.find_student(sid)
        org = self.orgDAO.find_org(oid)
        param={"student":stu,"organization":org}
        return self.is_exists(param,{},[])
