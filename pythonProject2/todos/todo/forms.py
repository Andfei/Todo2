from django import forms
from .models import Todo
from django.core.exceptions import ValidationError


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["id", "name", "description", "user", "complete"]


    def clean_title(self):
        if len(self.cleaned_data.get('name  ')) < 2:
            raise ValidationError('error')
        return self.cleaned_data.get('name')


class TodoUpdateForm(TodoForm):
    class Meta:
        model = Todo
        fields = ["id", "name", "description", "user", "complete"]

    def clean(self):
        clean_data = super().clean()
        clean_data['name'] = clean_data.get('name') or self.instance.name
        clean_data['description'] = clean_data.get('description') or self.instance.description
        clean_data['user'] = clean_data.get('user') or self.instance.user
        clean_data['complete'] = clean_data.get('complete') or self.instance.complete