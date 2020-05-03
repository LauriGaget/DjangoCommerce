from django.db import models
from django.urls import reverse
from users.models import UserCustom
from django.shortcuts import render, HttpResponseRedirect


class Category(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            unique=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE,
                                 )
    name = models.CharField(max_length=120)
    brand = models.CharField(max_length=120)
    price = models.FloatField()
    image = models.ImageField(blank=True)
    description = models.TextField(null=True)
    slug = models.SlugField(max_length=200, null=True)
    favori = models.ManyToManyField(UserCustom, related_name='favori', blank=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])





