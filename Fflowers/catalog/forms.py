from.models import Catalog
from.models import Subcategory
from django import forms



class ProductForm(forms.ModelForm):
    class Meta:
        model=Catalog
        fields=('name_product','price','show')


class CatForm(forms.ModelForm):
    class Meta:
        model=Subcategory
        fields='__all__'