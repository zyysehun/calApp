from django.db import models
from datetime import datetime

# Create your models here.


class Cal(models.Model):
    date = models.DateField()
    time = models.TimeField()
    # datetime = models.DateTimeField()
    wavelength = models.IntegerField()
    caldata = models.FloatField()

    def toDict(self):
        return {'id': self.id, 'datetime': self.datetime, 'wavelength': self.wavelength, 'caldata': self.caldata}

    class Meta:
        db_table = "tb_one"  # 更改表名


class Cal02(models.Model):
    date = models.DateField()
    time = models.TimeField()
    wavelength = models.IntegerField()
    caldata = models.FloatField()

    def toDict(self):
        return {'id': self.id, 'datetime': self.datetime, 'wavelength': self.wavelength, 'caldata': self.caldata}

    class Meta:
        db_table = "tb_two"  # 更改表名


class Cal03(models.Model):
    date = models.DateField()
    time = models.TimeField()
    wavelength = models.IntegerField()
    caldata = models.FloatField()

    def toDict(self):
        return {'id': self.id, 'datetime': self.datetime, 'wavelength': self.wavelength, 'caldata': self.caldata}

    class Meta:
        db_table = "tb_three"  # 更改表名


class Calhim(models.Model):
    date = models.DateField()
    time = models.TimeField()
    wavelength = models.IntegerField()
    diff = models.FloatField()
    global_irr = models.FloatField()
    direct = models.FloatField()
    dg_radio = models.FloatField()

    def toDict(self):
        return {'id': self.id, 'datetime': self.datetime, 'wavelength': self.wavelength, 'diff': self.diff, 'global_irr': self.global_irr, 'direct': self.direct, 'dg_radio': self.dg_radio}

    class Meta:
        db_table = "tb_him"  # 更改表名


class Spec01(models.Model):
    date = models.DateField()
    time = models.TimeField()
    # datetime = models.DateTimeField()
    wavelength = models.IntegerField()
    reflectance = models.FloatField()

    def toDict(self):
        return {'id': self.id, 'datetime': self.datetime, 'wavelength': self.wavelength, 'reflectance': self.reflectance}

    class Meta:
        db_table = "tb_spec01"  # 更改表名


class Spec02(models.Model):
    date = models.DateField()
    time = models.TimeField()
    # datetime = models.DateTimeField()
    wavelength = models.IntegerField()
    reflectance = models.FloatField()

    def toDict(self):
        return {'id': self.id, 'datetime': self.datetime, 'wavelength': self.wavelength, 'reflectance': self.reflectance}

    class Meta:
        db_table = "tb_spec02"  # 更改表名


class Spec03(models.Model):
    date = models.DateField()
    time = models.TimeField()
    # datetime = models.DateTimeField()
    wavelength = models.IntegerField()
    reflectance = models.FloatField()

    def toDict(self):
        return {'id': self.id, 'datetime': self.datetime, 'wavelength': self.wavelength, 'reflectance': self.reflectance}

    class Meta:
        db_table = "tb_spec03"  # 更改表名


class Psrv1(models.Model):
    date = models.DateField()
    time = models.TimeField()
    nm_340 = models.IntegerField()
    nm_380 = models.IntegerField()
    nm_440 = models.IntegerField()
    nm_500 = models.IntegerField()
    nm_675 = models.IntegerField()
    nm_870 = models.IntegerField()
    nm_937 = models.IntegerField()
    nm_1020 = models.IntegerField()
    nm_1640 = models.IntegerField()
    wktemp = models.FloatField()
    envitemp = models.FloatField()
    envihumi = models.FloatField()
    pressure = models.IntegerField()
    Inenvitemp = models.FloatField()
    Inenvihumi = models.FloatField()
    Headtemp = models.FloatField()
    Headhumi = models.FloatField()
    FQ1 = models.IntegerField()
    FQ2 = models.IntegerField()
    FQ3 = models.IntegerField()
    FQ4 = models.IntegerField()

    # def toDict(self):
    #     return {'id': self.id, 'datetime': self.datetime, 'wavelength': self.wavelength, 'reflectance': self.reflectance}

    class Meta:
        db_table = "tb_psrv1"  # 更改表名


class Psrv2(models.Model):
    date = models.DateField()
    time = models.TimeField()
    wZenith = models.FloatField()
    wAirmass = models.FloatField()
    wCloud = models.IntegerField()
    wAOD340 = models.FloatField()
    wAOD380 = models.FloatField()
    wAOD440 = models.FloatField()
    wAOD500 = models.FloatField()
    wAOD675 = models.FloatField()
    wAOD870 = models.FloatField()
    wAOD1020 = models.FloatField()
    wAOD1640 = models.FloatField()
    walpha = models.FloatField()
    wbeta = models.FloatField()
    wAOD550 = models.FloatField()
    wPW = models.FloatField()

    # def toDict(self):
    #     return {'id': self.id, 'datetime': self.datetime, 'wavelength': self.wavelength, 'reflectance': self.reflectance}

    class Meta:
        db_table = "tb_psrv2"  # 更改表名
