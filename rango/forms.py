from django import forms
from rango.models import Page, Category

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128), help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), inital=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), inital=0)
    slug = forms.CharField(widget=forms.hiddenInput(), required=False)

    #inline class that gives other info on the form

    class Meta:
        #provide association between the ModelForm and a model
        model = Category
        fields = ('name',)

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), inital=0)

    class Meta:
        #association again
        model = Page
        #hides the foreign key
        exclude = ('category',)

        #fields - specify which fields of model are included on the form
        #widgets - what we wish to use for each field to be displayed
        #   eg - in pageform class, we defined forms.charfield for title etc
        #   these fields provide text entry for users
        # the hidden things let us set default values, for views and likes etc
        # still need to include hidden stuff - could get exceptions otherwise by model
        # avoids null errors - need to be careful. slug not required cos we handled it earlier
        

