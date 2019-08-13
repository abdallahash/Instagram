from django import forms 
from .models import Post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field 
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions
)


# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post 
#         fields = [
#             'image',
#             'caption',
#         ]

class PostForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Post', 'Post', css_class='btn-primary'))

    class Meta:
        model = Post 
        fields = [
            'image',
            'caption'
        ]