from django import forms
from django.contrib.auth.models import User
from pages.models import Region, Place, Building, Character

# selectable app import
import selectable.forms as selectable

from pages.lookups import PlaceLookup, BuildingLookup


class RegionForm(forms.ModelForm):
    name = forms.CharField(max_length=200, help_text="Please enter the region name.")
    description = forms.CharField(widget=forms.Textarea, help_text="Please describe the region.")

    class Meta:
        model = Region
        fields = ('name',)
        exclude = ('description',)


class PlaceForm(forms.ModelForm):
    name = forms.CharField(max_length=200, help_text="Name:")
    region = forms.ModelChoiceField(
        queryset=Region.objects.all(),
        required=True,
        empty_label=('Select a region'),
    )
    population = forms.IntegerField(initial=0, help_text='Population:')
    description = forms.CharField(widget=forms.Textarea, help_text='Description:')
    economy = forms.CharField(widget=forms.Textarea, help_text='Economy:')
    special_features = forms.CharField(widget=forms.Textarea, help_text='Special Features:')

    class Meta:
        model = Place
        fields = ('name', 'region', 'population', 'description', 'economy', 'special_features')
        exclude = ('',)


class CharacterForm(forms.ModelForm):
    place_list = Place.objects.all()
    building_list = Building.objects.all()

    name = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Name'
            }
        ),
    )

    # Chain select the following three selects
    region = forms.ModelChoiceField(
        queryset=Region.objects.all(),
        required=True,
        empty_label=('Select a region'),
    )

    # place = selectable.AutoCompleteSelectField(
    #     lookup_class=PlaceLookup,
    #     label='Place',
    #     required=False,
    #     # widget=selectable.AutoComboboxSelectWidget,
    #     widget=selectable.AutoCompleteSelectWidget,
    # )

    # building = selectable.AutoCompleteSelectField(
    #     lookup_class=BuildingLookup,
    #     label='Building',
    #     required=False,
    #     # widget=selectable.AutoComboboxSelectWidget,
    #     widget=selectable.AutoCompleteSelectWidget,
    #     # widget=forms.Select,
    # )

    # Old select drop downs.
    place = forms.ModelChoiceField(Place.objects, widget=forms.Select, empty_label="-- Places --")
    building = forms.ModelChoiceField(Building.objects, widget=forms.Select, empty_label="-- Buildings --")

    # race
    RACES = (
        ('', '-- Race --'),
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
    race = forms.ChoiceField(
        choices=RACES,
        help_text='Race',
    )

    # stats
    strength = forms.IntegerField(help_text='strength', initial=9)
    stamina = forms.IntegerField(help_text='stamina', initial=9)
    speed = forms.IntegerField(help_text='speed', initial=9)
    agility = forms.IntegerField(help_text='agility', initial=9)
    toughness = forms.IntegerField(help_text='toughness', initial=9)
    constitution = forms.IntegerField(help_text='constitution', initial=9)
    intelligence = forms.IntegerField(help_text='intelligence', initial=9)
    logic = forms.IntegerField(help_text='logic', initial=9)
    teaching = forms.IntegerField(help_text='teaching', initial=9)
    intuition = forms.IntegerField(help_text='intuition', initial=9)
    beauty = forms.IntegerField(help_text='beauty', initial=9)
    charisma = forms.IntegerField(help_text='charisma', initial=9)
    leadership = forms.IntegerField(help_text='leadership', initial=9)

    # class
    CLASSES = (
        ('', '-- Class --'),
        ('Fighter', 'Fighter'),
        ('Thief', 'Thief'),
        ('Survivalist', 'Survivalist'),
        ('Cleric', 'Cleric'),
        ('Mage', 'Mage'),
        ('Mentalist', 'Mentalist'),
        ('Fighter/Thief', 'Fighter/Thief'),
        ('Fighter/Survivalist', 'Fighter/Survivalist'),
        ('Fighter/Cleric', 'Fighter/Cleric'),
        ('Fighter/Mage', 'Fighter/Mage'),
        ('Fighter/Mentalist', 'Fighter/Mentalist'),
        ('Thief/Survivalist', 'Thief/Survivalist'),
        ('Thief/Cleric', 'Thief/Cleric'),
        ('Thief/Mage', 'Thief/Mage'),
        ('Thief/Mentalist', 'Thief/Mentalist'),
        ('Survivalist/Cleric', 'Survivalist/Cleric'),
        ('Survivalist/Mage', 'Survivalist/Mage'),
        ('Survivalist/Mentalist', 'Survivalist/Mentalist'),
        ('Cleric/Mage', 'Cleric/Mage'),
        ('Cleric/Mentalist', 'Cleric/Mentalist'),
        ('Mage/Mentalist', 'Mage/Mentalist'),
    )
    character_class = forms.ChoiceField(
        # max_length=255,
        choices=CLASSES,
        # default='Fighter',
    )

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
        fields = (
            'name', 'region', 'place', 'building', 'race',
            'strength', 'stamina', 'speed', 'agility', 'toughness', 'constitution', 'intelligence', 'logic', 'teaching', 'intuition', 'beauty', 'charisma'
        )

    # class CharacterForm(forms.Form):

    # def __init__(self, *args, **kwargs):
    #     super(CharacterForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_id = 'id-exampleForm'
    #     self.helper.form_class = 'blueForms'
    #     self.helper.form_method = 'post'
    #     self.helper.form_action = 'submit_survey'

    #     self.helper.add_input(Submit('submit', 'Submit'))


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
