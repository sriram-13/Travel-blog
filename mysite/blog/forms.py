from django import forms


METHOD_CHOICES = (
    ('title', 'Title'),
    ('date', 'Published Date'),
    ('keyword', 'Keywords'),
)


class ArchivesForm(forms.Form):
    method = forms.ChoiceField(choices=METHOD_CHOICES)
    title = forms.CharField()
    published_date = forms.DateField()
    
