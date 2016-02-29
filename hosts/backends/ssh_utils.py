# -*- encoding:utf-8 -*-
"""
Create By : Zhenyu Liao
Create Date : 16/2/3
Update Date :
"""

import time
import paramiko
from hosts import models
from django.utils import timezone

def paramiko_ssh(task_id, host_obj, cmd):
    #print int(host_obj.host.port)
    bind_host = host_obj
    print bind_host
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        if bind_host.host_user.auth_type == "ssh-password":
            s.connect(bind_host.host.ip_addr,
                      int(bind_host.host.port),
                      bind_host.host_user.user_name,
                      bind_host.host_user.password,
                      timeout=5)

        else:
            print "ssh-key authentication"

        stdin, stdout, stderr = s.exec_command(cmd)
        res = stdout.read(), stderr.read()
        cmd_result = filter(lambda x:len(x) > 0, res)[0]
        result = 'success'

    except Exception, e:
        print "\033[31;1m%s\033[0m" % e
        cmd_result = e
        result = "failed"

    # 将命令执行结果写入到TaskLog表中
    log_write_obj = models.TaskLog.objects.get(child_of_task_id = task_id, bind_host_id = bind_host.id) # 获取任务记录
    log_write_obj.date = timezone.now() # 更新时间
    log_write_obj.event_log = cmd_result
    log_write_obj.result = result

    log_write_obj.save() # 保存
