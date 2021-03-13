from django import forms
import datetime


class PublicationForm(forms.Form):
    required_css_class = 'required'
    title = forms.CharField(max_length=1000, label="Publication Title", required="true", label_suffix='')
    url = forms.CharField(max_length=2048, label="URL", required="false", label_suffix='')
    journal = forms.CharField(max_length=1000, required="false", label_suffix='')
    conference = forms.CharField(max_length=1000, required="false", label_suffix='')
    year = forms.IntegerField(label="Year of Publication", widget=forms.TextInput, min_value=1000, max_value=datetime.datetime.now().year, required="true", label_suffix='')
    abstract = forms.CharField(widget=forms.Textarea, required="true", label_suffix='')
    hidden = forms.BooleanField(label="Should the publication be hidden?", required="false", label_suffix='')
