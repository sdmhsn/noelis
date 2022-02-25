from django.forms import ModelForm
from .models import Article, Review
from django import forms
from tinymce.widgets import TinyMCE


class ArticleForm(ModelForm):
    body = forms.CharField(widget=TinyMCE)

    class Meta:
        model = Article
        fields = '__all__'
        exclude = ['owner', 'vote_total', 'vote_ratio']
        widgets = {
            'categories': forms.CheckboxSelectMultiple(
                attrs={
                    'style': 'margin-right: 1rem;',
                }
            )
        }

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Add title'})


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']
        labels = {
            'value': 'Place your vote',
            'body': 'Add a comment with your vote'
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
