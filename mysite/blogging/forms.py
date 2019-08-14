from django.forms import ModelForm
from blogging.models import Post

# Establishg the Post Form
class MyPostForm(ModelForm):

    class Meta:
        # Define the Model on which to draw and it's associated fields. 
        model = Post
        fields = ['title', 'text', 'author']