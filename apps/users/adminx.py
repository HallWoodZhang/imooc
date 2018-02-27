# _*_ coding: utf-8 _*_

import xadmin

from .models import EmailVerifyRecord
from .models import Banner

class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type',]
    list_filter = list_display


class BannerAdmin(object):
    # title = models.CharField(max_length=100, verbose_name=u'标题')
    # image = models.ImageField(max_length=100, upload_to='banner/%Y/%m', verbose_name=u'轮播图')
    # url = models.URLField(max_length=200, verbose_name=u'访问地址')
    # index = models.IntegerField(default=100, verbose_name=u'顺序')
    # add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')
    list_display = ['image', 'title', 'url', 'index', 'add_time']
    search_fields = ['image', 'title', 'url', 'index']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
