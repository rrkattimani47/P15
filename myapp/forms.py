from django import forms
from myapp.models import *

class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields=('topic','name','url')#'__all__'
        #exclude=('url',)