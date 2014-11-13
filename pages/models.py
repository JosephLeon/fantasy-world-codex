from django.db import models


class Region(models.Model):
    region_name = models.Charfield(max_length=200)


class Place(models.Model):
    region = models.ForeignKey(Region)
    place_name = models.Charfield(max_length=200)


class Building(models.Model):
    region = models.ForeignKey(Region)
    place = models.ForeignKey(Place)
    building_name = models.Charfield(max_length=200)


class Character(models.Model):
    place = models.ForeignKey(Place)
    building = models.ForeignKey(Building)
    character_name = models.Charfield(max_length=200)


class Item(models.Model):
    place = models.ForeignKey(Place)
    building = models.ForeignKey(Building)
    character = models.ForeignKey(Character)
    item_name = models.Charfield(max_length=200)
