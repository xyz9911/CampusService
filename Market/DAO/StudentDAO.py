from .BaseDAO import BaseDAO
from ..models import *


class StudentDAO(BaseDAO):
    MODEL_CLASS = Student

    def add_student(self, stu):
        return self.save(stu)

    def update_student(self, stu):
        return self.update(stu)

    def add_student_info(self, info):
        return self.save(info)

    def get_student(self, sid):
        param = {"id": sid}
        return self.find_one(param, {},[])

    def get_all_students(self):
        return self.find_queryset()


class StudentInfoDAO(BaseDAO):
    MODEL_CLASS = StudentInfo
    stuDAO = StudentDAO()

    def add_info(self, info):
        return self.save(info)

    def update_info(self, info):
        return self.save(info)

    def get_info(self, sid):
        stu = self.stuDAO.get_student(sid)
        param = {"student": stu}
        return self.find_one(param, {},[])