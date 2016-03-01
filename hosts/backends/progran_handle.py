#!/usr/bin/env python
# -*- encoding:utf-8 -*-
'''
Create By : Zhenyu Liao
Create date : 
Update date :  
'''

# django 程序调用外部脚本，首先要加入到环境变量里面去，同事需要设置django setup
import os, sys, django
BaseDir = "/".join(os.path.dirname(os.path.abspath(__file__)).split("\\")[:-2])
#print BaseDir
sys.path.append(BaseDir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LZYOPS.settings")
django.setup()

import multiprocessing
from hosts import models
from django.core.exceptions import ObjectDoesNotExist
import paramiko, time, multiprocessing
from django.utils import timezone


def program_update(task_id, task_type):
    """
    更新程序处理函数：
    """
    # print 'program_update:', task_id, task_type
    try:
        pool = multiprocessing.Pool(processes=5) # 定义进程池

        selected_host_id_list = models.TaskInfo.objects.get(id = task_id).hosts.select_related()
        print 'selected_host_id_list:',type(selected_host_id_list)
        for h in selected_host_id_list:
            target_host_ip = str(h.host.ip_addr)
            pool.apply_async(parmiko_ssh, args=(task_id, task_type, target_host_ip))

        pool.close()
        pool.join()

    except ObjectDoesNotExist, e:
        print e


def program_callback(task_id, task_type):
    """
    回滚程序处理函数：
    """
    print 'program_callback:', task_id


def parmiko_ssh(task_id, task_type, target_host_ip):
    print "oh yes! parmiko_ssh:::", task_id, task_type, target_host_ip

if __name__ == '__main__':
    required_args = ['-task_id', '-task_type']
    for arg in required_args:
        if not arg in sys.argv:
            sys.exit('Arg [ %s ] is required!' % arg)

    if len(sys.argv) < 4:
        sys.exit("Two arguments args expected but %s given!" % len(sys.argv))

    task_id = sys.argv[sys.argv.index('-task_id') + 1]
    task_type = sys.argv[sys.argv.index('-task_type') + 1]
    #print task_id, task_type

    if hasattr(__import__(__name__), task_type):
        func = getattr(__import__(__name__), task_type)
        func(task_id, task_type)
    else:
        sys.exit("Invalid task_type, just support [program_update, program_callback]!")