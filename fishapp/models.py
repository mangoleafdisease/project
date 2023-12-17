from django.core.validators import validate_comma_separated_integer_list
from django.db import models


# Create your models here.


FISH_MODELS = [
    ("Abu Garcia 6'6 ft Salty Fighter ", "Abu Garcia 6'6 ft Salty Fighter "),
    ("Neon Blue Wagtail Platy Fish", "Neon Blue Wagtail Platy Fish"),
    ("Mickey Mouse Platy Fish", "Mickey Mouse Platy Fish"),
    ("Parrot Platy Fish", "Parrot Platy Fish"),
    ("Hifin Tuxedo Yellow Platy Fish", "Hifin Tuxedo Yellow Platy Fish"),
]


FISH_COLORS = [
    ("Gold", "Gold"),
    ("Yellow", "Yellow"),
    ("Black", "Black"),
    ("Gray", "Gray"),
    ("Light Yellow", "Light Yellow"),
]


FISH_SIZES = [
    ("37", "37"),
    ("38", "38"),
    ("39", "39"),
    ("40", "40"),
    ("41", "41"),
    ("42", "42"),
    ("43", "43"),
    ("44", "44"),
    ("45", "45"),
    ("46", "46"),
]


class Fish(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50, choices=FISH_MODELS)
    price = models.IntegerField()
    size = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    color = models.CharField(max_length=20, choices=FISH_COLORS)

    def __str__(self):
        return self.name
