from django.db import models

class Content(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)
    contributors = models.ManyToManyField('Contributor',
                                          related_name='content_contributor')
    pub_date = models.DateTimeField('date published')


class Article(Content):
    content = models.ForeignKey(Content, related_name='content_article')
    text = models.TextField()

    def show(self):
    	return '%s %s %s' % (self.content.title, self.content.subtitle, self.text)


class Image(Content):
    content = models.ForeignKey(Content, related_name='content_image')
    path = models.FilePathField(max_length=100)

    def info(self):
    	return '%s %s' % (self.content.title, self.content.subtitle)



class Contributor(models.Model):
    last_name = models.CharField(max_length=500)
    first_name = models.CharField(max_length=500)
    content = models.ManyToManyField(Content, related_name='contributor')

    def die(self):
    	self.delete()