# -*- encoding:utf-8 -*-
"""
Create By : Zhenyu Liao
Create Date : 16/1/28
Update Date :
"""
from django.db import transaction
import models
from LZYOPS import settings
import subprocess

class Task(object):

    def __init__(self, request):
        self.request = request
        self.task_type = self.request.POST.get('task_type')

    def handle(self):
        if self.task_type:
            print self.task_type
            if hasattr(self, self.task_type):
                func = getattr(self, self.task_type)
                return func()
            else:
                raise TypeError

    @transaction.atomic
    def multi_cmd(self):
        # 批量命令执行函数,负责处理前端提起的任务请求
        #print "====Begin to excute cmd!===="

        cmd = self.request.POST.get("cmd_text")
        selected_hosts = self.request.POST.getlist("selected_host[]")
        #print "=====>", self.task_type, selected_hosts, cmd
        # create task info
        task_obj = models.TaskInfo(
            task_type = self.task_type,
            user_id = self.request.user.id,
            cmd = cmd,
            # manytomany 必须在创建完后再添加
        )
        task_obj.save()
        task_obj.hosts.add(*selected_hosts) # 列表形式前面加*,传入列表的每一个值

        # 在taskInfo表里面创建任务信息时,同事初始化一条到TaskLog表
        for bind_host_id in selected_hosts:
            obj = models.TaskLog(
                child_of_task_id = task_obj.id,
                bind_host_id = bind_host_id,
                event_log = "N/A",
            )
            obj.save()

        # invoke multi_task script-- 调用 multi_task.py 脚本
        p = subprocess.Popen([
            'python', settings.MultiTaskScript,
            '-task_id', str(task_obj.id),
            '-run_type', settings.MultiTaskType,
        ])

        return {'task_id': task_obj.id}

    @transaction.atomic
    def program_update(self):
        print '=====>Ready to:program_update'
        print 'task_type: ', self.task_type
        print 'User id:', self.request.user.id
        selected_hosts = self.request.POST.getlist('host_id_list[]')
        # print selected_hosts

        # 在数据库创建任务信息记录
        task_obj = models.TaskInfo(
            task_type = self.task_type,
            user_id = self.request.user.id,
        )
        task_obj.save()
        task_obj.hosts.add(*selected_hosts) # 列表形式前面加*,传入列表的每一个值

        # 在taskInfo表里面创建任务信息时,同事初始化一条到TaskLog表
        for bind_host_id in selected_hosts:
            obj = models.TaskLog(
                child_of_task_id = task_obj.id,
                bind_host_id = bind_host_id,
                event_log = "N/A",
            )
            obj.save()
        # invoke multi_task script-- 调用 multi_task.py 脚本
        p = subprocess.Popen([
            'python', settings.ProgramHandleScript,
            '-task_id', str(task_obj.id),
        ])

        '''
        for bind_host_id in selected_hosts:
            print models.BindHostToUser.objects.get(id = bind_host_id)
            selected_host_id = models.BindHostToUser.objects.get(id = bind_host_id).host_id
            selected_host_ip = models.Host.objects.get(id = selected_host_id).ip_addr
            print selected_host_ip
        '''
        return {'task_id': task_obj.id}



    def get_task_result(self):
        # 从数据库获取任务日志,返回给前端
        task_id = self.request.GET.get('task_id')
        if task_id:
            res_list = models.TaskLog.objects.filter(child_of_task_id=task_id)
            return list(res_list.values(
                'id',
                'bind_host__host__host_name',
                'bind_host__host__ip_addr',
                'bind_host__host_user__user_name',
                'date',
                'event_log',
                'result'
            ))