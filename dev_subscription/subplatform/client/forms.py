from django.forms import ModelForm

from account.models import CustomUser

class UpdateUserForm(ModelForm):    ## make sure we import model form

    password = None

    class Meta:

        model = CustomUser
        fields = ['email', 'first_name', 'last_name',]
        exclude = ['password1', 'password2',]