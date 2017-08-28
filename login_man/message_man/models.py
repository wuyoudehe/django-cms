from django.db import models
from django.utils import timezone
# Create your models here.
from man_log import models as mmode


# 信息发送时间 信息标题 信息内容  信息发送人  信息接收人  信息状态
class message_man(models.Model):
	time = models.DateTimeField('datatime', default=timezone.now)
	message_title = models.CharField(max_length=40)
	message_txt = models.TextField(max_length=40)
	message_sendname = models.CharField(max_length=150)
	message_recivename = models.CharField(max_length=150)
	message_status = models.IntegerField( default=1)


