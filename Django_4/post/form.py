from django import forms
from .models import Post,Comment


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        # fields=["title","context","puplish_date"] #model'de auto_now_add=True oldugu için formda bu alana mudahale etmiyoruz.
        fields=["title","context","image"]


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        # fields=["title","context","puplish_date"] #model'de auto_now_add=True oldugu için formda bu alana mudahale etmiyoruz.
        fields=[
            "name",
            "comment"
            ]