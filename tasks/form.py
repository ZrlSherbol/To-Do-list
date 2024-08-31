from django import forms

class TaskForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=100)
    category = forms.CharField(max_length=50)

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        if title == "puthon":
            raise forms.ValidationError("title is required")
        return cleaned_data

        if title and content and title.lower() == content.lower():
            raise forms.ValidationError("title is required")
        return cleaned_data
    def clean_title(self):
        title = self.cleaned_data['title']
        if 'puthon' in title.lower():
            raise forms.ValidationError("title is required")
        return title