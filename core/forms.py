from django import forms

from core.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['creator']

    def __init__(self, *args, **kwargs):
        self.creator = kwargs.pop('creator', None)
        super().__init__(*args, **kwargs)
        for (name, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control mb-3'



# class PostForm(forms.Form):
#     title = forms.CharField(max_length=20)
#     description = forms.Textarea()
#     image = forms.ImageField(upload_to='images')
#     git_link = forms.URLField()
#     tags = forms.CharField(max_length=100)
#     creator = forms.ForeignKey(UserProfile, on_delete=models.CASCADE)