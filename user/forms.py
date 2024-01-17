from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserAccount

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'required'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id': 'required'}))
    phone_number = forms.CharField(max_length=12)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number']
        model.is_active = False
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        phone_number = cleaned_data.get('phone_number')
        if User.objects.filter(username=username).exists():
            self.add_error('username', 'This username is already taken. Please choose a different username.')
        if UserAccount.objects.filter(phone_number=phone_number).exists():
            self.add_error('phone_number', 'This phone number is already registered. Please use a different phone number.')
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit == True:
            user.is_active = False
            user.save()
            phone_number = self.cleaned_data.get('phone_number')
            UserAccount.objects.create(
                user=user,
                phone_number=phone_number,
            )
        return user

class UserUpdateForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=12)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance:
            try:
                user_account = self.instance.user
            except UserAccount.DoesNotExist:
                user_account = None

            if user_account:
                self.fields['phone_number'].initial = user_account.phone_number

    def save(self, commit=True):
        user = super().save(commit=False)

        if commit:
            user.save()

            user_account, created = UserAccount.objects.get_or_create(user=user)

            user_account.phone_number = self.cleaned_data['phone_number']
            user_account.save()

        return user
