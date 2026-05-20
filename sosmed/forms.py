from django import forms
from django.contrib.auth.models import User

class AkunForm(forms.ModelForm):
    first_name = forms.CharField(label="First Name", required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Last Name", required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name']

    def save(self, commit=True):
        user = super().save(commit=False)
        # Automatically generate the required username field in the background
        user.username = f"{self.cleaned_data['first_name'].lower()}_{self.cleaned_data['last_name'].lower()}"
        if commit:
            user.save()
        return user
