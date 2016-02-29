#!/usr/bin/env python
# -*- encoding:utf-8 -*-
'''
Create By : Zhenyu Liao
Create date : 
Update date :  
'''

# django 程序调用外部脚本，首先要加入到环境变量里面去，同事需要设置django setup
import os, sys, django
BaseDir = "/".join(os.path.dirname(os.path.abspath(__file__)).split("/")[:-2])
print BaseDir