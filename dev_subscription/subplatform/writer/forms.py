from . models import Article

from account.models import CustomUser

from django.forms import ModelForm

class ArticleForm(ModelForm):   ## will fill in html

    class Meta:
        model = Article
        fields = ['title', 'content', 'is_premium',]


class UpdateUserForm(ModelForm):    ## exclude password
    password = None

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name',]
        exclude = ['password1', 'password2',]


