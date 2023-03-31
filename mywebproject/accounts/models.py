from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Article(models.Model):
    # Article model for storing information about a blog post

    # Title of the article, maximum length is 100 characters
    title = models.CharField(max_length=100)

    # Summary of the article
    summary = models.TextField()

    # Body of the article
    body = models.TextField()

    # Date when the article was posted, automatically set to the current date and time
    date_posted = models.DateTimeField(auto_now_add=True)

    # Author of the article, represented by a foreign key to the User model
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        # String representation of the Article object, returns the title of the article
        return self.title

    def get_absolute_url(self):
        # Returns the URL for the detail view of an Article instance
        # Reverse function constructs the URL by looking up the 'article_detail' URL pattern
        # and passing the primary key of the Article instance as a keyword argument
        return reverse('article_detail', kwargs={'pk': self.pk})
