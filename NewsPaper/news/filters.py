from django_filters import FilterSet, AllValuesFilter, ModelChoiceFilter
from .models import Post, Author
from django import forms


class PostFilter(FilterSet):
    created_time = AllValuesFilter(widget=forms.Select(attrs={'class': 'form-control mb-2'}))
    author = ModelChoiceFilter(queryset=Author.objects.all(),
                                    widget=forms.Select(attrs={'class': 'form-control mb-2'})
                                    )

    class Meta:
        model = Post
        fields = ('created_time', 'author')