from django.db import models

class User(models.Model):
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
class Role(models.Model):
    roleid = models.SmallIntegerField(primary_key=True,max_length=8)
    name = models.CharField(max_length=30)

class Class(models.Model):
    classid = models.SmallIntegerField(primary_key=True,max_length=8)
    name = models.CharField(max_length=30)

class RatingRank1(models.Model):
    name = models.CharField(max_length=30)
    describe = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class RatingRank2(models.Model):
    name = models.CharField(max_length=30)
    point = models.IntegerField()
    describe = models.CharField(max_length=120)
    rank1id =models.ForeignKey(
            'RatingRank1',on_delete=models.CASCADE,)

    def __str__(self):
        return self.name

class RatingModel(models.Model):
    name = models.CharField(max_length=30)
    startdate = models.DateField()
    enddate = models.DateField()
    ratinglist = models.json
    describe = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class RatingModeltoUser(models.Model):
    ratingmodelid = models.ForeignKey(
            'RatingModel',on_delete=models.CASCADE,)
    uid = models.ForeignKey(
            'User',on_delete=models.CASCADE,)


class RatingForm(models.Model):
    ratingformid = models.AutoField()
    name = models.CharField(max_length=30)
    ratingmodelid = models.IntegerField()
    uid = models.IntegerField()
    ratinglist = models.json
    ratingdate = models.DateTimeField()
    updatetime = models.DateTimeField(auto_now=True)




    
