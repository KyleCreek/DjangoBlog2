from django.contrib.syndication.views import Feed
from django.urls import reverse
from blogging.models import Post

class LatestEntriesFeed(Feed):
    title = "Latest Entries in my Blog"
    link = "/"
    description = 'Latest Entries in the Blog'

    def items(self):
        return Post.objects.order_by('created_date')[:3]
    
    def item_title(self, item):
        return item.title
    
    def item_text(self, item):
        return item.text

    def item_link(self, item):
        return reverse('', args=[item.pk])
