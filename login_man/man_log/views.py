from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.http import HttpResponse, HttpResponseRedirect
from man_log.models import User
import json
from django.contrib.auth.decorators import login_required


def register(request):
	redirect_to = request.POST.get('next', request.GET.get('next', ''))
	# 只有当请求为 POST 时，才表示用户提交了注册信息
	if request.method == 'POST':
		# request.POST 是一个类字典数据结构，记录了用户提交的注册信息
		# 这里提交的就是用户名（username）、密码（password）、邮箱（email）
		# 用这些数据实例化一个用户注册表单
		form = RegisterForm(request.POST)

		# 验证数据的合法性
		if form.is_valid():
			# 如果提交数据合法，调用表单的 save 方法将用户数据保存到数据库
			form.save()
			if redirect_to:
				return redirect(redirect_to)
			else:
				return HttpResponseRedirect('/content/')
			# 注册成功，跳转内容管理页面
			return HttpResponseRedirect('/content/')
	else:
		# 请求不是 POST，表明用户正在访问注册页面，展示一个空的注册表单给用户
		form = RegisterForm()

	# 渲染模板
	# 如果用户正在访问注册页面，则渲染的是一个空的注册表单
	# 如果用户通过表单提交注册信息，但是数据验证不合法，则渲染的是一个带有错误信息的表单
	return render(
		request,
		'man_log/register.html',
		context={
			'form': form,
			'next': redirect_to})

@login_required
def logout(request):
	return render(request, 'man_log/logout.html')


def login(request):
	return render(request, 'registration/login.html')

def index(request):
	return render(request,'index.html')


@login_required
def content(request):
	usersnames = User.objects.all()
	mannames = {'username': []}
	for x in usersnames:

		mannames['username'].append(x.username)
	return render(request, 'content.html', {'mannames': json.dumps(mannames)})