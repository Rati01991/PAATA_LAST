from django import forms
from .models import Car

class AddCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['make', 'model', 'year', 'price_per_day', 'available']

class SearchForm(forms.Form):
    make = forms.CharField(required=False)
    model = forms.CharField(required=False)
    min_year = forms.IntegerField(required=False)
    max_price = forms.DecimalField(required=False)


from django import forms
from .models import UserSubmittedCar

class UserCarSubmissionForm(forms.ModelForm):
    class Meta:
        model = UserSubmittedCar
        fields = ['make', 'model', 'year', 'price_per_day', 'owner_name', 'owner_email', 'description']