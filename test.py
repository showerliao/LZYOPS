#!/usr/bin/env python
# -*- encoding:utf-8 -*-
'''
Create By : Zhenyu Liao
Create date : 
Update date :  
'''

import time
import datetime
d = datetime.datetime(2016, 2, 16, 3, 57, 36)
print d
unixtime = time.mktime(d.timetuple())
print unixtime