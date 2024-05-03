from django import forms
from .models import Comments



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ("writer", "comment", "article") 
        widgets = {
            "article": forms.HiddenInput(),
            "writer":  forms.HiddenInput(),

        }
