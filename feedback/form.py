from django import forms
from .models import Feedback


# class FeedbackForm(forms.Form):
#     name = forms.CharField(label='Имя', max_length=7, min_length=2, error_messages={
#         'max_length': 'Слишком много символов',
#         'min_length': 'Слишком мало символов',
#         'required': 'Вы ничего не ввели',
#
#     })
#     rating = forms.IntegerField(label='Оценка от 1 до 5', min_value=1, max_value=5)
#     surname = forms.CharField(label='Фамилия')
#     feedback = forms.CharField(label='Отзыв', widget=forms.Textarea(attrs={'rows': 2, 'cols': 20}))

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        # fields = ['name', 'surname', 'rating', 'feedback']
        fields = '__all__'
        labels = {
            'name': 'Имя',
            'surname': 'Фамилия',
            'rating': 'Оценка от 1 до 5',
            'feedback': 'Отзыв',
        }
        error_messages = {
            'name': {
                'max_length': 'Слишком много символов',
                'min_length': 'Слишком мало символов',
                'required': 'Поле не должно быть пустым',
            },
            'surname': {
                'max_length': 'Слишком много символов',
                'min_length': 'Слишком мало символов',
                'required': 'Поле не должно быть пустым',
            },
            'feedback': {
                'max_length': 'Слишком много символов',
                'min_length': 'Слишком мало символов',
                'required': 'Поле не должно быть пустым',
            }
        }


