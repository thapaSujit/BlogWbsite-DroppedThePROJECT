from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    # This is a Django form that inherits from forms.ModelForm
    # It allows us to create a form that is automatically generated from a model

    class Meta:
        model = Article
        # We are setting the model for this form to be the Article model
        # This means that the fields in the form will be generated from the Article model

        fields = ['title', 'summary', 'body']
        # We are specifying which fields from the Article model we want to include in the form
        # In this case, we want the title, summary, and body fields to be included