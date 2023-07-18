from typing import Any
from django.forms import ModelForm,Textarea
from .models import Review,Book

class ReviewForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'form-control'})
        self.fields['watchAgain'].widget.attrs.update({'class': 'form-check-input'})

    class Meta:
            model = Review
            fields = ['text','watchAgain']
            labels = {'watchAgain': 'Read Again'}
            widgets ={'text':Textarea(attrs={'rows':4})}

class AddBookForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(AddBookForm, self).__init__(*args, **kwargs)
        for fieldname in ['title','description','image','url']:
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})   
        
    class Meta:
        model = Book
        fields = '__all__'

