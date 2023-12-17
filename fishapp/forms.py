from django import forms
from .models import Fish

FISH_MODELS = [
    ("Gold Red Platy Fish", "Gold Red Platy Fish"),
    ("Neon Blue Wagtail Platy Fish", "Neon Blue Wagtail Platy Fish"),
    ("Mickey Mouse Platy Fish", "Mickey Mouse Platy Fish"),
    ("Parrot Platy Fish", "Parrot Platy Fish"),
    ("Hifin Tuxedo Yellow Platy Fish", "Hifin Tuxedo Yellow Platy Fish"),
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

FISH_COLORS = [
    ("Gold", "Gold"),
    ("Yellow", "Yellow"),
    ("Black", "Black"),
    ("Gray", "Gray"),
    ("Light Yellow", "Light Yellow"),
]


class FishForm(forms.ModelForm):
    size = forms.TextInput(attrs={'class': 'form-control'})
    image = forms.ImageField()

    class Meta:
        model = Fish
        fields = ('name', 'model', 'price', 'size', 'color', 'image')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.Select(attrs={'class': 'form-control'}, choices=FISH_MODELS),
            'price': forms.TextInput(attrs={'class': 'form-control'}),

            'color': forms.Select(attrs={'class': 'form-control'}, choices=FISH_COLORS),
        }
