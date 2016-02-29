#!/usr/bin/env python
# -*- encoding:utf-8 -*-
'''
Create By : Zhenyu Liao
Create date : 
Update date :  
'''

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.utils import timezone

class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password,
            date_of_birth=date_of_birth
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    job_number = models.IntegerField(u"工号", blank=True, default=None, null=True)
    name = models.CharField(u"姓名", max_length=64, blank=True, default=None, null=True)
    department = models.CharField(u"部门", max_length=64, blank=True, default=None, null=True)
    position = models.CharField(u"职位", max_length=64, blank=True, default=None, null=True)
    mobile = models.CharField(u"手机", max_length=32, blank=True, default=None, null=True)
    memo = models.TextField(u"备注", blank=True, null=True, default=None)
    add_date = models.DateTimeField(auto_now_add=True, blank=True)

    host_groups = models.ManyToManyField("HostGroup", blank=True)
    bind_hosts = models.ManyToManyField("BindHostToUser", blank=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = u"用户信息"

    def get_full_name(self):
        # The user is identified by their email address
        return self.email, self.job_number, self.name, self.department, self.position

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin