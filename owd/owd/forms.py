from django import forms
from django.core import validators


def must_be_empty(value):
    if value:
        raise forms.ValidationError('is not empty')

class ContactForm(forms.Form):
	"""Form to contact OWD's support email."""
	name = forms.CharField(label="", help_text="", 
		widget=forms.TextInput(attrs={'placeholder': 'Name'}))
	company = forms.CharField(label="", help_text="", 
		widget=forms.TextInput(attrs={'placeholder': 'Company'}))
	email = forms.EmailField(label="", help_text="", 
		widget=forms.TextInput(attrs={'placeholder': 'Email'}))
	verify_email = forms.EmailField(label="", help_text="", 
		widget=forms.TextInput(attrs={'placeholder': 'Verify email'}))
	subject = forms.CharField(label="", help_text="", 
		widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
	message = forms.CharField(label="", help_text="", 
		widget=forms.Textarea(attrs={'placeholder': 'Message'}))
	honeypot = forms.CharField(required=False,
                               widget=forms.HiddenInput,
                               label="Leave empty",
                               validators=[must_be_empty]
                              )


	def clean(self):
		cleaned_data = super(ContactForm, self).clean()
		if len(cleaned_data) == 1:
			raise forms.ValidationError("All fields are required.")
		email = cleaned_data['email']
		verify = cleaned_data['verify_email']

		if email != verify:
			raise forms.ValidationError("You need to enter the same email in both fields.")

