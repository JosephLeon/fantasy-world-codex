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
    place = models.ForeignKey(Place)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    contents = models.TextField(blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Character(models.Model):
    region = models.ForeignKey(Region, blank=True, null=True)
    place = models.ForeignKey(Place, blank=True, null=True)
    building = models.ForeignKey(Building, blank=True, null=True)
    name = models.CharField(max_length=200)

    # race
    RACES = (
        ('Human', 'Human'),
        ('Dwarf', 'Dwarf'),
        ('Elf', 'Elf'),
        ('Halfling', 'Halfling'),
        ('Human/Dwarf', 'Human/Dwarf'),
        ('Human/Elf', 'Human/Elf'),
        ('Human/Halfling', 'Human/Halfling'),
        ('Dwarf/Elf', 'Dwarf/Elf'),
        ('Dwarf/Halfling', 'Dwarf/Halfling'),
        ('Elf/Halfling', 'Elf/Halfling'),
        ('Gunder', 'Gunder'),
        ('Orc', 'Orc'),
        ('Goblin', 'Goblin'),
        ('Human/Orc', 'Human/Orc'),
        ('Dwarf/Orc', 'Dwarf/Orc'),
        ('Elf/Orc', 'Elf/Orc'),
    )
    race = models.CharField(
        max_length=255,
        choices=RACES,
        default='Human',
    )

    # stats
    strength = models.IntegerField(default=12)
    stamina = models.IntegerField(default=12)
    speed = models.IntegerField(default=12)
    agility = models.IntegerField(default=12)
    toughness = models.IntegerField(default=12)
    constitution = models.IntegerField(default=12)
    intelligence = models.IntegerField(default=12)
    logic = models.IntegerField(default=12)
    teaching = models.IntegerField(default=12)
    intuition = models.IntegerField(default=12)
    beauty = models.IntegerField(default=12)
    charisma = models.IntegerField(default=12)
    leadership = models.IntegerField(default=12)


    def __str__(self):
        return self.name


class Item(models.Model):
    place = models.ForeignKey(Place, blank=True, null=True)
    building = models.ForeignKey(Building, blank=True, null=True)
    character = models.ForeignKey(Character)
    item_name = models.CharField(max_length=200)

    def __str__(self):
        return self.item_name
