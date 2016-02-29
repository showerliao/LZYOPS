# -*- encoding:utf-8 -*-
"""
Create By : Zhenyu Liao
Create Date : 16/2/2
Update Date :
"""

import os, sys, django
BaseDir = "/".join(os.path.dirname(os.path.abspath(__file__)).split("/")[:-2])
sys.path.append(BaseDir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LZYOPS.settings")
django.setup()

import multiprocessing
from hosts import models
from django.core.exceptions import ObjectDoesNotExist
from ssh_utils import paramiko_ssh

def by_paramiko(task_id):
    try:
        task_obj = models.TaskInfo.objects.get(id=task_id)
        pool = multiprocessing.Pool(processes=5)

        for h in task_obj.hosts.select_related():
            pool.apply_async(paramiko_ssh, args=(task_id, h, task_obj.cmd))

        pool.close()
        pool.join()

    except ObjectDoesNotExist, e:
        print(e)


if __name__ == '__main__':
    required_args = ['-task_id', '-run_type']

    for arg in required_args:
        if not arg in sys.argv:
            sys.exit('Arg [ %s ] is required!' % arg)

    if len(sys.argv) < 5:
        sys.exit("Five arguments args expected but %s given!" % len(sys.argv))

    task_id = sys.argv[sys.argv.index('-task_id') + 1]
    run_type = sys.argv[sys.argv.index('-run_type') + 1]

    if hasattr(__import__(__name__), run_type):
        func = getattr(__import__(__name__), run_type)
        func(task_id)
    else:
        sys.exit("Invalid run_type, just support [by_paramiko, by_ansible, by_saltstack]")