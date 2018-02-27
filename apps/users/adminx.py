# _*_ coding: utf-8 _*_

import xadmin
from xadmin import views

from .models import EmailVerifyRecord, Banner


class BaseSetting(object):
    enable_themes = True
    use_booswatch = True


class GlobalSetting(object):
    site_title = u'imooc后台'
    site_footer = u'hallwood_zhang@163.com'
    menu_style = 'accordion'


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type',]
    list_filter = list_display


class BannerAdmin(object):
    list_display = ['image', 'title', 'url', 'index', 'add_time']
    search_fields = ['image', 'title', 'url', 'index']
    list_filter = list_display


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
