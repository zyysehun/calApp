from django.db import models
from datetime import datetime

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=50)  # 员工账号
    nickname = models.CharField(max_length=50)  # 昵称
    password_hash = models.CharField(max_length=100)  # 密码
    password_salt = models.CharField(max_length=50)  # 密码干扰值
    status = models.IntegerField(default=1)  # 状态:1正常/2禁用/6管理员/9删除
    create_at = models.DateTimeField(default=datetime.now)  # 创建时间
    update_at = models.DateTimeField(default=datetime.now)  # 修改时间

    def toDict(self):
        return {'id': self.id, 'username': self.username, 'nickname': self.nickname, 'password_hash': self.password_hash, 'password_salt': self.password_salt, 'status': self.status, 'create_at': self.create_at.strftime('%Y-%m-%d %H:%M:%S'), 'update_at': self.update_at.strftime('%Y-%m-%d %H:%M:%S')}

    class Meta:
        db_table = "user"  # 更改表名


class Cal(models.Model):
    # date = models.DateField()
    # time = models.TimeField()
    datetime = models.DateTimeField()
    wavelength = models.IntegerField()
    caldata = models.FloatField()

    def toDict(self):
        return {'id': self.id, 'datetime': self.datetime, 'wavelength': self.wavelength, 'caldata': self.caldata}

    class Meta:
        db_table = "tb_one"  # 更改表名


class Cal02(models.Model):
    # date = models.DateField()
    # time = models.TimeField()
    datetime = models.DateTimeField()
    wavelength = models.IntegerField()
    caldata = models.FloatField()

    def toDict(self):
        return {'id': self.id, 'datetime': self.datetime, 'wavelength': self.wavelength, 'caldata': self.caldata}

    class Meta:
        db_table = "tb_two"  # 更改表名


class Cal03(models.Model):
    # date = models.DateField()
    # time = models.TimeField()
    datetime = models.DateTimeField()
    wavelength = models.IntegerField()
    caldata = models.FloatField()

    def toDict(self):
        return {'id': self.id, 'datetime': self.datetime, 'wavelength': self.wavelength, 'caldata': self.caldata}

    class Meta:
        db_table = "tb_three"  # 更改表名


class Calhim(models.Model):
    # date = models.DateField()
    # time = models.TimeField()
    datetime = models.DateTimeField()
    wavelength = models.IntegerField()
    diff = models.FloatField()
    global_irr = models.FloatField()
    direct = models.FloatField()
    dg_radio = models.FloatField()

    def toDict(self):
        return {'id': self.id, 'datetime': self.datetime, 'wavelength': self.wavelength, 'diff': self.diff, 'global_irr': self.global_irr, 'direct': self.direct, 'dg_radio': self.dg_radio}

    class Meta:
        db_table = "tb_him"  # 更改表名
