from django.conf.urls import url, include
from .views.StudentViews import *
from .views.NoticeViews import *
from .views.OrgViews import *

urlpatterns = [
    url(r'^insert_student$', insert_student),
    url(r'^update_student$', update_student),
    url(r'^remove_student$', remove_student),
    url(r'^show_student$', show_student),
    url(r'^insert_student_info$', insert_student_info),
    url(r'^update_student_info$', update_student_info),
    url(r'^show_student_info$', show_student_info),
    url(r'^remove_student_info$', remove_student_info),
    url(r'^invite_student_to_org$', invite_student_to_org),
    url(r'^remove_student_from_org$', remove_student_from_org),
    url(r'^show_student_in_orgs$', show_student_in_orgs),
    url(r'^show_orgs_of_stus$', show_orgs_of_stus),
    url(r'^is_member$', is_member),
    url(r'^is_charger$', is_charger),

    url(r'^post_notice$', post_notice),
    url(r'^show_notice$', show_notice),
    url(r'^remove_notice$', remove_notice),
    url(r'^read_notice$', read_notice),
    url(r'^show_notice_by_org$', show_notice_by_org),
    url(r'^show_unread_notice$', show_unread_notice),
    url(r'^show_read_notice$', show_read_notice),

    url(r'^post_org$', post_org),
    url(r'^update_org$', update_org),
    url(r'^remove_org$', remove_org),
    url(r'^show_org$', show_org),
    url(r'^show_all_orgs$', show_all_orgs),
    url(r'^add_stu_as_charge$', add_stu_as_charge),
    url(r'^remove_stu_as_charge$', remove_stu_as_charge),
    url(r'^update_stu_charge$', update_stu_charge),
    url(r'^show_orgs_charges$', show_orgs_charges),
]