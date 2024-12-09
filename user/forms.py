from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı")
    password = forms.CharField(label="Parola", widget=forms.PasswordInput)

    



class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=3, label="Kullanıcı Adını Giriniz ")
    password = forms.CharField(max_length=20, min_length=8, label="Parola  ", widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=20, min_length=8, label="Parolayı Doğrula  ", widget=forms.PasswordInput)

    def clean(self):
        # program çalışmazsa üstteki kodu sil self.cleaned_data yap alttakileri
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            # forms.ValidationError olarak değiştir
            raise forms.ValidationError("Parola Doğrulama Başarısız !!!")
        values = {
            "username" : username,
            "password" : password
        }
        return values
    