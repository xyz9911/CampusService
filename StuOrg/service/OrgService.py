from ..DAO.OrgDAO import *


class OrgService:
    def __init__(self):
        self.orgDAO = OrgDAO()
        self.orgChargeDAO = OrgChargeDAO()

    def add_org(self, oname, oimage, odes):
        if not self.orgDAO.add_org(oname, oimage, odes):
            raise Exception("insert error")
        return True

    def find_org(self, oid):
        return self.orgDAO.find_org(oid)

    def remove_org(self, oid):
        if not self.orgDAO.remove_org(oid):
            raise Exception("remove error")
        return True

    def find_all_orgs(self):
        return self.orgDAO.find_all_orgs()

    def update_org(self, oid, oname, oimage, odes):
        if not self.orgDAO.update_org(oid, oname, oimage, odes):
            raise Exception("update error")
        return True

    def add_stu_as_charge(self, oid, sid, sduty):
        if not self.orgChargeDAO.add_charge(oid, sid, sduty):
            raise Exception("insert error")
        return True

    def remove_stu_charge(self, oid, sid):
        if not self.orgChargeDAO.remove_charge(oid, sid):
            raise Exception("remove error")
        return True

    def update_charge(self, oid, sid, sduty):
        if not self.orgChargeDAO.update_charge(oid, sid, sduty):
            raise Exception("update error")
        return True

    def find_charge_by_org(self, oid):
        return self.orgChargeDAO.find_charge_by_org(oid)
