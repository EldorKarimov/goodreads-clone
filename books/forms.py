from django import forms
from .models import Comment

class AddCommentForm(forms.ModelForm):
    stars_given = forms.IntegerField(min_value=1, max_value=5)
    class Meta:
        model = Comment
        fields = ('text', 'stars_given')
