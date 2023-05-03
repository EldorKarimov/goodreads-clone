from django import forms
from .models import CustomUser

class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(
        attrs={
            'type':'password'
        }
    )
    )
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save()