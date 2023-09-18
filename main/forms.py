from django.forms import ModelForm
from main.models import Flower

class FlowerForm(ModelForm):
    class Meta:
        model = Flower
        fields = ["name", "amount", "description"]