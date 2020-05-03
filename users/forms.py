from django_registration.forms import RegistrationForm
from users.models import UserCustom


class UserForm(RegistrationForm):

    class Meta(RegistrationForm.Meta):
        model = UserCustom