from django.db import models

class Content(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500)
    contributors = models.ManyToManyField('Contributor',
                                          related_name='content_contributor')
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.title


class Article(Content):
    text = models.TextField()

    def show(self):
    	return '%s %s %s' % (self.title, self.subtitle, self.text)


class Image(Content):
    path = models.ImageField(upload_to="image_path")

    def info(self):
    	return '%s %s' % (self.title, self.subtitle)

class Gallery(Content):
    images = models.ManyToManyField(Image, related_name='gallery_image')

class Contributor(models.Model):
    last_name = models.CharField(max_length=500)
    first_name = models.CharField(max_length=500)
    content = models.ManyToManyField(Content, related_name='contributor_content')
    def __str__(self):
        return self.first_name + " " + self.last_name

    def die(self):
    	self.delete()