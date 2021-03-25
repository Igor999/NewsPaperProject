from django.db import models


class Author(models.Model):
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    rating = models.IntegerField()
    one_to_one_user = models.OneToOneField(models.user)
    # user = models.ForeignKey(models.user, on_delete=models.CASCADE)

class Category(models.Model):
    category_name = models.CharField(max_length=255)
    category_name.unique = True


class Post(models.Model):
    choice = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)
    news_heading = models.CharField(max_length=255)
    news_text = models.CharField(max_length=255)
    news_rating = models.IntegerField()
    one_to_one_Author = models.OneToOneField(Author)
    many_to_many_Category = models.ManyToManyField(Category)

    def ratplus(self):
        news_rating = self.Post.news_rating
        return (news_rating+1)
    def ratminus(self):
        news_rating = self.Post.news_rating
        return (news_rating-1)

    def preview(selfself):
        news_text_preview = self.Post.news_text
        return news_text_preview[0:125]

class PostCategory(models.Model):
    many_to_many_relation = models.ManyToManyField(Category)
    many_to_many_relation = models.ManyToManyField(Post)


class Comment(models.Model):
    comment_text = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)
    comment_rating = models.IntegerField()
    one_to_many_relation = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(models.user, on_delete=models.CASCADE)

    def Complus(self):
        comment_rating = self.Post.comment_rating
        return (comment_rating+1)
    def Comminus(self):
        comment_rating = self.Post.comment_rating
        return (comment_rating-1)
