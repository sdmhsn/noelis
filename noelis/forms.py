from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.forms import SetPasswordForm



# For password reset form
class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class UserSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(UserSetPasswordForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})