from django.db import models
# from django.contrib.auth.models import User


class Region(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Place(models.Model):
    region = models.ForeignKey(Region)
    name = models.CharField(max_length=200)
    population = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    economy = models.TextField(blank=True)
    special_features = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Building(models.Model):
    region = models.ForeignKey(Region)
    place = models.ForeignKey(Place, blank=True, null=True)
    place_name = models.CharField(max_length=200)

    def __str__(self):
        return self.place_name


class Character(models.Model):
    region = models.ForeignKey(Region, blank=True, null=True)
    place = models.ForeignKey(Place, blank=True, null=True)
    building = models.ForeignKey(Building, blank=True, null=True)
    character_name = models.CharField(max_length=200)

    def __str__(self):
        return self.character_name


class Item(models.Model):
    place = models.ForeignKey(Place, blank=True, null=True)
    building = models.ForeignKey(Building, blank=True, null=True)
    character = models.ForeignKey(Character)
    item_name = models.CharField(max_length=200)

    def __str__(self):
        return self.item_name
