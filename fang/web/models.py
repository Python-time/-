from django.db import models

# Create your models here.
from django.db import models


class Fang(models.Model):
    title = models.CharField(max_length=255)
    # 连接
    link = models.CharField(max_length=255)
    # 小区
    community = models.CharField(max_length=255)
    # 居室
    housetype = models.CharField(max_length=255)
    # 朝向
    direction = models.CharField(max_length=255)
    # 楼层
    floor = models.CharField(max_length=255)
    # 区域//div[@class="areaName"]//span/a/text()
    region = models.CharField(max_length=255)
    # 总价
    totalPrice = models.CharField(max_length=255)
    # 关注人数
    followInfo = models.CharField(max_length=255)
    # 单价
    unitPrice = models.CharField(max_length=255)
    # 面积
    acreage = models.CharField(max_length=255)
    # 看房次数
    frequency = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'fang'
class Hot(models.Model):
    kw = models.CharField(max_length=30)
    #居室
    cat_choice = [
        (1, '区域'),
        (2, '居室'),
        (3, '总价格'),
        (4, '面积'),
    ]
    cat = models.IntegerField(choices=cat_choice, default=1)
    status = models.IntegerField(default=1)
    # 权重越大，排名靠前
    weight = models.IntegerField(default=1)

    def __str__(self):
        return self.kw


    class Meta:
        verbose_name_plural = verbose_name = '查询关键词'
