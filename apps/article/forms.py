from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'message', 'image']
        exclude = ['article']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your Name', 'id': 'name'})
        self.fields['message'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your Message', 'id': 'message', 'rows': 10, 'cols': 30})
        self.fields['image'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Upload Image', 'id': 'image'}) 