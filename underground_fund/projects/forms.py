from django import forms
from .models import Projects, Image

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = [
            "title",
            "description",
            "deadline"
        ]

class ImageForm(forms.ModelForm):
    image = forms.ImageField(
        label = "image",
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
    )

    class Meta:
        model = Image
        fields = ("image",)

