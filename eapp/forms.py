from django import forms

from .models import Product,Profile

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'details', 'image']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded px-4 py-2 focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter product name'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'w-full border border-gray-300 rounded px-4 py-2 focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter price'
            }),
            'details': forms.Textarea(attrs={
                'class': 'w-full border border-gray-300 rounded px-4 py-2 h-32 focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter product details'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'w-full border border-gray-300 rounded px-4 py-2 bg-white'
            }),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields = ['image']
