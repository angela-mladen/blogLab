from django import forms
from .models import BlogPost


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"
           # self.fields['date'].widget=forms.widgets.DateInput(
            #    attrs={
            #        'type':'date','placeholder':'yyyy-mm-dd(DOB)',
              #      'class':'form-control'
             #   }
           # )

    class Meta:
        model = BlogPost
        exclude = ("user",)