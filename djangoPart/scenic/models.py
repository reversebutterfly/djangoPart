from django.db import models

class ScenicSpot(models.Model):
    name = models.CharField(max_length=200, verbose_name='景点名称')
    region = models.CharField(max_length=100, verbose_name='地区')
    score = models.FloatField(default=0, verbose_name='评分')
    star = models.CharField(max_length=50, default='无', verbose_name='评级')
    address = models.CharField(max_length=300, blank=True, verbose_name='地址')
    comment = models.TextField(blank=True, verbose_name='评语')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='价格')
    sale = models.IntegerField(default=0, verbose_name='销量')
    province_city_region = models.CharField(max_length=100, verbose_name='省市自治区')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '旅游景点'
        verbose_name_plural = '旅游景点列表'
        ordering = ['-score', '-sale']