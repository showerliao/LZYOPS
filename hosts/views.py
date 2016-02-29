# -*- encoding:utf-8 -*-

from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
import models, task, json, utils

def index(request):
    return render(request, "index.html")

@login_required
def hosts(request):
    return render(request, 'hosts/host.html')

@login_required
def assets(request):
    return render(request, 'assets/assets.html')

@login_required
def monitor(request):
    return render(request, 'monitor/monitor.html')

@login_required
def acc_logout(request):
    logout(request)
    return HttpResponseRedirect(request, "/")

def acc_login(request):
    login_error_msg = ''
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        #print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/")
        else:
            login_error_msg = u"错误的用户名或密码!请重新输入!"
    return render(request, 'login.html', {'login_error_msg': login_error_msg})

@login_required
def host_manage(request):
    # 获取前端页面当前选择的主机组ID
    selected_gid = request.GET.get('selected_gid')

    if selected_gid: # 如果主机组ID不为空,返回该主机组下面的主机
        host_list = models.BindHostToUser.objects.filter(host_groups__id=selected_gid)
    else: # 如果主机组ID为空,则返回未分组的主机
        host_list = request.user.bind_hosts.select_related()
    return render(request, "hosts/host_manage.html", {'host_list': host_list})

@login_required
def multi_cmd(request):
    return render(request, "hosts/multi_cmd.html")

@login_required
def submit_task(request):
    print request.POST
    task_obj = task.Task(request)
    res = task_obj.handle()
    return HttpResponse(json.dumps(res))

@login_required
def get_task_result(request):
    # 获取任务执行结果,返回给前端
    task_obj = task.Task(request)
    res = task_obj.get_task_result()
    return HttpResponse(json.dumps(res, default=utils.jsonDateFormat))

@login_required
def file_transfer(request):
    return render(request, "hosts/file_transfer.html")

@login_required
def program_handle(request):
    return render(request, "hosts/program_handle.html")

