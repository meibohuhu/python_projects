
from django.contrib.auth.forms import UserCreationForm


from account.models import CustomUser

class CreateUserForm(UserCreationForm):
    class Meta:     ## require you to enter in the model => CustomUser => will save into DB
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2', 'is_writer']

