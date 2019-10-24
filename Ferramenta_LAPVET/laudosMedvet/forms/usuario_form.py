from django.forms import ModelForm
from django import forms


from laudosMedvet.models import UsuarioModel, UserModel


class UserForm(ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'required': True}
        )
    )

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()

    class Meta:
        model = UserModel
        exclude = ('email', 'date_joined', 'is_staff', 'user_permissions', 'groups', 'is_active')


class UsuarioForm(ModelForm):

    class Meta:
        model = UsuarioModel
        fields = ['data_nasc', 'cpf', 'rg', 'telefone', 'celular', 'email',
                  'endereco', 'numero', 'bairro', 'cidade', 'estado']