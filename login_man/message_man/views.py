from django.shortcuts import render, HttpResponse
from .models import message_man
import json, time
from django.contrib.auth.decorators import login_required


# Create your views here.

#  接收网页a、b、receivename3个参数
@login_required
def message_ajax(request):
    a = request.POST.get('a', 1)
    b = request.POST.get('b', 1)
    receivename = request.POST.get('receivename', 1)
    if a is not None and b is not None and receivename is not None:
        m = message_man.objects.create(
            message_title=a,
            message_txt=b,
            message_recivename=receivename,
            message_sendname=str(
                request.user),
            message_status=2)
        m.save()
        return HttpResponse(
            json.dumps({"name": "success", "year": time.ctime()}),
            content_type="application/json"
        )




# 根据提交的当前用户  提取未读邮件 并将内容传递给前台
@login_required
def message_num(request):
    weidu_messages = message_man.objects.filter(
        message_recivename=str(request.user), message_status=2
    )
    msg_title = []
    msg_content = []
    msg_sendname = []
    msg_time = []
    for x in weidu_messages:
        msg_title.append(x.message_title)
        msg_content.append(x.message_txt)
        msg_sendname.append(x.message_sendname)
        msg_time.append(str(x.time))
    return render(request, 'registration/message.html', {'msg_title':msg_title,'msg_content':msg_content,'msg_sendname':msg_sendname,'msg_time':msg_time})
