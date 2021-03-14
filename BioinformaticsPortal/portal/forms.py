from django import forms
import datetime

from django.forms import Widget


class PublicationForm(forms.Form):
    required_css_class = 'required_label'
    title = forms.CharField(max_length=1000, label="Publication Title", required="true", label_suffix='')
    url = forms.URLField(max_length=2048, label="URL", required="false", label_suffix='')
    pubType = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'custom-select', 'onchange': 'updateTypeName(this)'}),
        choices=[('journal', 'Journal Entry'), ('conference', 'Conference Paper')],
        label="Type of Publication")
    typeName = forms.CharField(max_length=1000, label_suffix='', label='Journal Name')
    year = forms.IntegerField(label="Year of Publication", widget=forms.TextInput, min_value=1000,
                              max_value=datetime.datetime.now().year, required="true", label_suffix='')
    abstract = forms.CharField(widget=forms.Textarea, required="true", label_suffix='')
    hidden = forms.BooleanField(initial=False, label="Should the publication be hidden?", required=False,
                                label_suffix='')


class AuthorForm(forms.Form):
    required_css_class = 'required_label'
    name = forms.CharField(max_length=1000, label="Author Name", required=True, label_suffix='')
    email = forms.EmailField(label="Author Email", required=False, label_suffix='')
    corresponding = forms.BooleanField(initial=False,
                                       widget=forms.CheckboxInput(attrs={'onclick': 'updateCorresponding(this)'})
                                       ,
                                       label="Corresponding Author:",
                                       required=False,
                                       label_suffix='')
