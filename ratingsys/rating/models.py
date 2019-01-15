from django_mysql.models import Model,JSONField
from django.db import models

def jsonfield_default():
    return {'django':'mysql'}

# 用户信息表
class User(Model):
    uid = models.SmallIntegerField(primary_key=True,max_length=10,db_index=True)
    name = models.CharField(max_length=30,null=False)
    sexual = models.CharField(max_length=4,null=False)
    duty = models.BooleanField()
    roleid = models.ForeignKey(
            'Role',on_delete=models.CASCADE,)
    classid = models.ForeignKey(
            'Class',on_delete=models.CASCADE,)
    updatetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# 用户角色
class Role(Model):
    roleid = models.SmallIntegerField(primary_key=True,max_length=8)
    name = models.CharField(max_length=30)
# 班级名
class Class(Model):
    classid = models.SmallIntegerField(primary_key=True,max_length=8)
    name = models.CharField(max_length=30)

# 评测表一级条目
class RatingRank1(Model):
    name = models.CharField(max_length=30)
    describe = models.CharField(max_length=120)

    def __str__(self):
        return self.name
# 评测表二级条目
class RatingRank2(Model):
    name = models.CharField(max_length=30)
    point = models.IntegerField()
    describe = models.CharField(max_length=120)
    rank1id =models.ForeignKey(
            'RatingRank1',on_delete=models.CASCADE,)

    def __str__(self):
        return self.name

# 评测表模型
class RatingModel(Model):
    name = models.CharField(max_length=30)
    startdate = models.DateField()
    enddate = models.DateField()
    ratinglist = JSONField(default=jsonfield_default)
    describe = models.CharField(max_length=120)

    def __str__(self):
        return self.name

# 评测表模型和用户对应关系
class RatingModeltoUser(Model):
    ratingmodelid = models.ForeignKey(
            'RatingModel',on_delete=models.CASCADE,)
    uid = models.ForeignKey(
            'User',on_delete=models.CASCADE,)

# 评测表条目，每天一条
class RatingForm(Model):
    ratingformid = models.IntegerField()
    name = models.CharField(max_length=30)
    ratingmodelid = models.IntegerField()
    uid = models.IntegerField()
    ratinglist = JSONField(default=jsonfield_default)
    ratingdate = models.DateTimeField()
    updatetime = models.DateTimeField(auto_now=True)