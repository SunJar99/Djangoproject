from django import forms
from posts.models import Category, Post, Tag

class TitleContentValidationMixin:
    def validate_title_and_content(self, cleaned_data):
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")
        if title and content and (title.lower() == content.lower()):
            raise forms.ValidationError("Title and content should not be the same")
        return cleaned_data

    def validate_title(self, cleaned_data):
        title = cleaned_data.get("title")
        if title and title.lower() == "python":
            raise forms.ValidationError("Title can't be equal to 'python'")
        return title


class PostForm(forms.Form, TitleContentValidationMixin):
    image = forms.ImageField(required=False)
    title = forms.CharField()
    content = forms.CharField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())

    def clean(self):
        cleaned_data = super().clean()
        return self.validate_title_and_content(cleaned_data)

    def clean_title(self):
        cleaned_data = super().clean()
        return self.validate_title(cleaned_data)


class PostForm2(forms.ModelForm, TitleContentValidationMixin):
    class Meta:
        model = Post
        fields = ["title", "content", "category", "tags"]

    def clean(self):
        cleaned_data = super().clean()
        return self.validate_title_and_content(cleaned_data)

    def clean_title(self):
        cleaned_data = super().clean()
        return self.validate_title(cleaned_data)


class SearchForm(forms.Form):
    search_q = forms.CharField(required=False, label="Search")
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)