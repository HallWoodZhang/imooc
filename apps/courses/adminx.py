# _*_ coding: utf-8 _*_

import xadmin

from .models import Course, CourseResource, Lesson, Video

class CourseAdmin(object):
    list_display = ['name', 'desc', 'degree', 'detail', 'learn_time', 'students_nums', 'fav_nums', 'click_nums', 'add_time']
    search_fields = ['name', 'degree', 'desc', 'detail', 'students_nums', 'fav_nums', 'click_nums']
    list_filter = list_display


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course__name', 'name', 'download', 'add_time']



class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson__name', 'name', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
xadmin.site.register(Video, VideoAdmin)
