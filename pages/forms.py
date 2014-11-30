from django import forms
from django.contrib.auth.models import User
from pages.models import Region, Place, Character


class RegionForm(forms.ModelForm):
    name = forms.CharField(max_length=200, help_text="Please enter the region name.")
    description = forms.CharField(widget=forms.Textarea, help_text="Please describe the region.")

    class Meta:
        model = Region
        fields = ('name',)
        exclude = ('description',)


class PlaceForm(forms.ModelForm):
    name = forms.CharField(max_length=200, help_text="Name:")
    population = forms.IntegerField(initial=0, help_text='Population:')
    description = forms.CharField(widget=forms.Textarea, help_text='Description:')
    economy = forms.CharField(widget=forms.Textarea, help_text='Economy:')
    special_features = forms.CharField(widget=forms.Textarea, help_text='Special Features:')

    class Meta:
        model = Place
        fields = ('name', 'population', 'description', 'economy', 'special_features')


class CharacterForm(forms.ModelForm):
    # region = forms.ForeignKey(Region, blank=True, null=True)
    # place = forms.ForeignKey(Place, blank=True, null=True)
    # building = forms.ForeignKey(Building, blank=True, null=True)
    region_list = Region.objects.all()
    name = forms.CharField(max_length=200)
    region = forms.ModelChoiceField(queryset=region_list, empty_label="None")

    # # race
    # RACES = (
    #     ('Human', 'Human'),
    #     ('Dwarf', 'Dwarf'),
    #     ('Elf', 'Elf'),
    #     ('Halfling', 'Halfling'),
    #     ('Human/Dwarf', 'Human/Dwarf'),
    #     ('Human/Elf', 'Human/Elf'),
    #     ('Human/Halfling', 'Human/Halfling'),
    #     ('Dwarf/Elf', 'Dwarf/Elf'),
    #     ('Dwarf/Halfling', 'Dwarf/Halfling'),
    #     ('Elf/Halfling', 'Elf/Halfling'),
    #     ('Gunder', 'Gunder'),
    #     ('Orc', 'Orc'),
    #     ('Goblin', 'Goblin'),
    #     ('Human/Orc', 'Human/Orc'),
    #     ('Dwarf/Orc', 'Dwarf/Orc'),
    #     ('Elf/Orc', 'Elf/Orc'),
    # )
    # race = forms.CharField(
    #     max_length=255,
    #     choices=RACES,
    #     default='Human',
    # )

    # # stats
    # strength = forms.IntegerField(default=12)
    # stamina = forms.IntegerField(default=12)
    # speed = forms.IntegerField(default=12)
    # agility = forms.IntegerField(default=12)
    # toughness = forms.IntegerField(default=12)
    # constitution = forms.IntegerField(default=12)
    # intelligence = forms.IntegerField(default=12)
    # logic = forms.IntegerField(default=12)
    # teaching = forms.IntegerField(default=12)
    # intuition = forms.IntegerField(default=12)
    # beauty = forms.IntegerField(default=12)
    # charisma = forms.IntegerField(default=12)
    # leadership = forms.IntegerField(default=12)

    # # class
    # CLASSES = (
    #     ('Fighter', 'Fighter'),
    #     ('Thief', 'Thief'),
    #     ('Survivalist', 'Survivalist'),
    #     ('Cleric', 'Cleric'),
    #     ('Mage', 'Mage'),
    #     ('Mentalist', 'Mentalist'),
    #     ('Fighter/Thief', 'Fighter/Thief'),
    #     ('Fighter/Survivalist', 'Fighter/Survivalist'),
    #     ('Fighter/Cleric', 'Fighter/Cleric'),
    #     ('Fighter/Mage', 'Fighter/Mage'),
    #     ('Fighter/Mentalist', 'Fighter/Mentalist'),
    #     ('Thief/Survivalist', 'Thief/Survivalist'),
    #     ('Thief/Cleric', 'Thief/Cleric'),
    #     ('Thief/Mage', 'Thief/Mage'),
    #     ('Thief/Mentalist', 'Thief/Mentalist'),
    #     ('Survivalist/Cleric', 'Survivalist/Cleric'),
    #     ('Survivalist/Mage', 'Survivalist/Mage'),
    #     ('Survivalist/Mentalist', 'Survivalist/Mentalist'),
    #     ('Cleric/Mage', 'Cleric/Mage'),
    #     ('Cleric/Mentalist', 'Cleric/Mentalist'),
    #     ('Mage/Mentalist', 'Mage/Mentalist'),
    # )
    # character_class = forms.CharField(
    #     max_length=255,
    #     choices=CLASSES,
    #     default='Fighter',
    # )

    # # skills
    # skills = forms.TextField(blank=True)

    # # appearance
    # height = forms.CharField(max_length=50)
    # weight = forms.CharField(max_length=50)
    # color = forms.CharField(max_length=50)
    # description = forms.TextField(blank=True)

    # # wealth
    # gold = forms.IntegerField(default=1)

    class Meta:
        model = Character
        fields = ('name', 'region')


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
