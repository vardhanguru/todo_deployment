from django import forms

from .models import Todo

class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ['task', 'description']

        widgets = {
            'task':forms.TextInput(attrs={'placeholder':'Task Title'}),
            'description':forms.Textarea(attrs={'placeholder':'Description'})
        }