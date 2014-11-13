from django.db import models


class Region(models.Model):
    region_name = models.CharField(max_length=200)

    def __str__(self):
        return self.region_name


class Place(models.Model):
    region = models.ForeignKey(Region)
    place_name = models.CharField(max_length=200)

    def __str__(self):
        return self.place_name


class Building(models.Model):
    region = models.ForeignKey(Region)
    place = models.ForeignKey(Place)
    building_name = models.CharField(max_length=200)

    def __str__(self):
        return self.building_name


class Character(models.Model):
    place = models.ForeignKey(Place)
    building = models.ForeignKey(Building)
    character_name = models.CharField(max_length=200)

    def __str__(self):
        return self.character_name


class Item(models.Model):
    place = models.ForeignKey(Place)
    building = models.ForeignKey(Building)
    character = models.ForeignKey(Character)
    item_name = models.CharField(max_length=200)

    def __str__(self):
        return self.item_name
