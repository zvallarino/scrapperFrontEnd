from django import forms

class TwitterForm(forms.Form):
    phrase = forms.CharField( max_length=100,label="phrase")
    start_date = forms.DateField(required=False)
    end_date = forms.DateField(required=False)