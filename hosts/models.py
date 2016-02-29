# -*- encoding:utf-8 -*-

from django.db import models

from customAuth import MyUser


class Host(models.Model):
    """
    主机表定义
    """
    host_name = models.CharField(u"主机名", max_length=64)
    ip_addr = models.GenericIPAddressField(u"IP地址", unique=True) # ip地址具有唯一性
    port = models.IntegerField(u"端口", default=22)
    idc = models.ForeignKey('IDC')
    system_type_choice = (
        ('linux', 'Linux'),
        ('windows', 'Windows'),
    )
    system_type = models.CharField(u"系统类型", choices=system_type_choice, max_length=32, default="linux")
    enabled = models.BooleanField(default=True)
    memo = models.TextField(u"备注", blank=True, null=True)
    add_date = models.DateTimeField(u"添加时间", auto_now_add=True, blank=True)

    class Meta:
        verbose_name = u"主机"
        verbose_name_plural = u"主机"

    def __unicode__(self):
        return "%s(%s)" % (self.host_name, self.ip_addr)

class IDC(models.Model):
    """
    IDC机房表定义
    """
    name = models.CharField(unique=True, max_length=64)
    memo = models.TextField(u"备注", blank=True, null=True)

    class Meta:
        verbose_name = u"IDC机房"
        verbose_name_plural = u"IDC机房"

    def __unicode__(self):
        return self.name

class HostUser(models.Model):
    """
    远程用户表定义
    """
    auth_type_choice = (
        ("ssh-password", "SSH/PASSWORD"),
        ("ssh-key", "SSH/KEY")
    )
    auth_type = models.CharField(choices=auth_type_choice, default="ssh-password", max_length=64)
    user_name = models.CharField(unique=True, max_length=64)
    password = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        verbose_name = u"主机用户"
        verbose_name_plural = u"主机用户"

    def __unicode__(self):
        return "%s(%s)" % (self.user_name, self.auth_type)

class HostGroup(models.Model):
    """
    主机组表定义
    """
    name = models.CharField(unique=True, max_length=64)
    memo = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = u"主机组"
        verbose_name_plural = u"主机组"

    def __unicode__(self):
        return self.name

class BindHostToUser(models.Model):
    """
    主机与用户绑定关系表
    """
    host = models.ForeignKey("Host")
    host_user = models.ForeignKey("HostUser")
    #host_user = models.ManyToManyField("HostUser")
    host_groups = models.ManyToManyField("HostGroup")

    class Meta:
        verbose_name = u"主机与用户的绑定关系"
        verbose_name_plural = u"主机与用户的绑定关系"

    def __unicode__(self):
        return "%s:%s" % (self.host, self.host_user)

    def get_host_groups(self):
        return ','.join([g.name for g in self.host_groups.select_related()])

class TaskInfo(models.Model):
    '''
     日志信息表
    '''
    start_time = models.DateTimeField(auto_now_add=True)
    done_time = models.DateTimeField(null=True, blank=True)
    task_type_choices = (
        ('multi_cmd', 'CMD'),
        ('file_send', '文件上传'),
        ('file_get', '文件下载')
    )
    task_type = models.CharField(choices=task_type_choices, max_length=50)
    user = models.ForeignKey("HostUser")
    hosts = models.ManyToManyField("BindHostToUser")
    cmd = models.TextField()
    expire_time = models.IntegerField(default=30)
    task_pid = models.IntegerField(default=0)
    note = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return "taskId:%s cmd:%s" % (self.id, self.cmd)

    class Meta:
        verbose_name = u"批量任务"
        verbose_name_plural = u"批量任务"

class TaskLog(models.Model):
    # 任务日志表
    child_of_task = models.ForeignKey("TaskInfo")
    bind_host = models.ForeignKey("BindHostToUser")
    date = models.DateTimeField(auto_now_add=True) # 任务完成时间
    event_log = models.TextField()
    result_choices = (
        ("success", "Success"),
        ("failed", "Failed"),
        ('unknown', "Unknown")
    )
    result = models.CharField(choices=result_choices, max_length=30, default='Unknown')
    note = models.TextField(max_length=100, blank=True)

    def __unicode__(self):
        return "child of:%s result:%s" % (self.child_of_task.id, self.result)

    class Meta:
        verbose_name = u"批量任务日志"
        verbose_name_plural = u"批量任务日志"