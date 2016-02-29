
from django.conf.urls import include, url
import views

urlpatterns = [
    url(r"^$", views.hosts, name="hosts"),
    url(r"^host_manage/$", views.host_manage, name="host_manage"),
    url(r"^multi_cmd/$", views.multi_cmd, name="multi_cmd"),
    url(r"^submit_task/$", views.submit_task, name="submit_task"),
    url(r"^get_task_result/$", views.get_task_result, name="get_task_result"),
    url(r"^file_transfer/$", views.file_transfer, name="file_transfer"),
    url(r"^program_handle/$", views.program_handle, name="program_handle"),
]
