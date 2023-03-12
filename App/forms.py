from django import forms
from .models import Custom

class CustomForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-field'}))
    class Meta:
        model = Custom
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Instagram Username'}),
            'country': forms.Select(attrs={'class': 'input-field',}),
           
        }