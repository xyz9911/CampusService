from .BaseDAO import BaseDAO
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
        info = self.find_info(sid)
        info.SSEX=ssex
        info.SMAJOR=smajor
        info.SINTRO=sintro
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
