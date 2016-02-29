# -*- encoding:utf-8 -*-
"""
Create By : Zhenyu Liao
Create Date : 16/2/1
Update Date :
"""

def jsonDateFormat(date):
    if hasattr(date, 'isoformat'):
        return date.strftime("%Y-%m-%d %H:%M:%S")