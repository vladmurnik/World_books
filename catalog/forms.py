from django import forms
from datetime import date

class AuthorsForm(forms.Form):
    first_name = forms.CharField(label='First Name author')
    last_name = forms.CharField(label="Last Name author")
    date_of_birth = forms.DateField(label="Date of Birth",
                                    initial=format(date.today()),
                                    widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    date_of_death = forms.DateField(label="Date of Death",
                                    initial=format(date.today()),
                                    widget=forms.widgets.DateInput(attrs={'type': 'date'}))
