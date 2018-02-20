from django import forms


class NamePhoneForm(forms.Form):
    name = forms.CharField(label='name_field', max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Введите Ваше имя', 'class': 'field'}))
    phone = forms.CharField(label='number_field', max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Введите Ваш номер', 'class': 'field'}))


class DetailPhoneForm(forms.Form):
    detail = forms.CharField(label='name_field', max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Введите название детали', 'class': 'field'}))
    phone = forms.CharField(label='number_field', max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Введите Ваш номер', 'class': 'field'}))


class QuizPhoneForm(forms.Form):
    quiz = forms.CharField(label='name_field', max_length=300, widget=forms.TextInput(attrs={'placeholder': 'Введите текст вопроса', 'class': 'field'}))
    phone = forms.CharField(label='number_field', max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Введите Ваш номер', 'class': 'field'}))
