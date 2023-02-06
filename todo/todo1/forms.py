from django import forms
from .models import alluser, alljob

class registForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = alluser
        fields = ('name','password')
        labels = {
            'name': ('account'),
            'password': ('password')
        }
    def clean_password(self,*args,**kwargs):
        password = self.cleaned_data.get('password')
        if len(password) <= 8:
            raise forms.ValidationError('aleast 9 characters!')
        elif hasLowerAndUpper(password) == False:
            raise forms.ValidationError('need lower and upper!')
        elif len(password) > 20:
            raise forms.ValidationError('max 20 characters!')
        return password

class loginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = alluser
        fields = ("name","password")
        labels = {
            'name': 'account',
            'password': 'password'
        }

def hasLowerAndUpper(text):
    has = [False,False]
    for i in text:
        if i.isupper():
            has[0] = True
        elif i.islower():
            has[1] = True
    if has == [True,True]:
        return True
    return False