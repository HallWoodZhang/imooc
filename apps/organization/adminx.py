# _*_ coding: utf-8 _*_

import xadmin

from .models import CityDict, CourseOrg, Teacher


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_nums', 'fav_nums', 'address', 'city', 'add_time']
    search_fields = ['name', 'desc', 'click_nums', 'fav_nums', 'address', 'city']
    list_filter = ['name', 'desc', 'click_nums', 'fav_nums', 'address', 'city__name', 'add_time']


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = list_display


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'fav_nums', 'click_nums', 'add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'fav_nums', 'click_nums']
    list_filter = ['org__name', 'name', 'work_years', 'work_company', 'work_position', 'points', 'fav_nums', 'click_nums', 'add_time']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
