from django import forms
from blog.models import Post, Comment


class PostForm(forms.ModelForm):
    is_agree = forms.BooleanField(label='약관동의', error_messages={'required' : "약관에 동의해주십쇼"})


    class Meta:
        model = Post
        #fields = '__all__'
        fields = ['title','content','photo','phone','tags']



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']

"""
class PostForm1(forms.Form):
title = forms.CharField()
content = forms.CharField(widget=forms.Textarea)
def save(self, commit=True):
post = Post(title= self.cleaned_data['title'], content=
self.cleaned_data['content'])
if commit:
post.save()
return post

"""







"""
html form

<form action == "" method = "post" >

<input type = "text" name = "title"/>

<textarea name = "content"> </textarea>
<input type = "submit"/>
</form>


"""
