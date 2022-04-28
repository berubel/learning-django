# Importing the serilizers module
from rest_framework import serializers

from .models import Post
from django import forms

# Structures how we would define a form

# That is the basically exactly the same for creating a serializer
'''
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title', 'description'
        )
'''
# A serializer basically just means transformation between our post model into a JSON payload
# that contains these two fields on that model. In the backend it will then look at these field
# and what kind of fields they are. Working with serializer we don't need package and dumping anything
# into json, it's all handled for us.
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title', 'description'
        )