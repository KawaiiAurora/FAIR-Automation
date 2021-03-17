from django import forms
import datetime
from portal.models import PublicationAuthor
from django.core.exceptions import ValidationError
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
    name = forms.CharField(widget=forms.TextInput(attrs={'onchange': 'updateTextValue(this)'}),
                           max_length=255, label="Author Name", required=True, label_suffix='')
    surname = forms.CharField(widget=forms.TextInput(attrs={'onchange': 'updateTextValue(this)'}),
                              max_length=255, label="Author Surname", required=True, label_suffix='')
    email = forms.EmailField(widget=forms.TextInput(attrs={'onchange': 'updateTextValue(this)'}),
                             label="Author Email", required=True, label_suffix='')
    corresponding = forms.BooleanField(initial=False,
                                       widget=forms.CheckboxInput(attrs={'class': 'w-auto'})
                                       ,
                                       label="Corresponding Author:",
                                       required=False,
                                       label_suffix='')

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        name = cleaned_data.get("name")
        surname = cleaned_data.get("surname")
        # If one inputs an existing author, checks that all the e-mail address given is associated with the proper
        # name/surname
        author = PublicationAuthor.objects.filter(email=email).first()
        if author is not None:
            if author.name != name or author.surname != surname:
                self.add_error("email",
                               ValidationError("An author with the same e-mail address but different "
                                               "details already exists!"))
