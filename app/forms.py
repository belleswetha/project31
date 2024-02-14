from typing import Any
from django import forms 


def validate_for_a(data):
    if data.lower().startswith('a'):
        raise forms.ValidationError('started with a')
    
def validate_for1_len(data):
    if len(data)<5:
        raise forms.ValidationError('len is max 5')


class SchoolForm(forms.Form):
    sname=forms.CharField(validators=[validate_for_a,validate_for1_len])
    sprinciple=forms.CharField(validators=[validate_for1_len])
    slocation=forms.CharField() 
    email=forms.EmailField()
    reenteremail=forms.EmailField()
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput)
    
    def cleaned_botcatcher(self):
        b=self.cleaned_data['botcatcher']
        if len(b)>0:
            raise forms.ValidationError('botcatcher')
     
     
    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['reenteremail']
        if e!=re:
            raise forms.ValidationError("wrong email check one's")

       