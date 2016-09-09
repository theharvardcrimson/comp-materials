# from django.http import Http4040
from django.shortcuts import get_object_or_404, render
from models import Author, BlogPost


# Returns a webpage showing a BlogPost matching a specific post_id
def blog_post(request, post_id):
    # Get post matching post_id or raise a HTTP 404 error
    post = get_object_or_404(BlogPost, id=post_id)

    # post = get_object_or_404(BlogPost, id=post_id) is basically the same as
    # post = None
    # try:
    #     post = BlogPost.objects.filter(id=post_id)[0]
    # except IndexError:
    #     raise Http404

    data = {'post': post}
    return render(request, 'blog_post.html', data)


# Returns a webpage showing a list of all BlogPosts in the database
def all_posts(request):
    # Find all blog posts
    data = {'posts': BlogPost.objects.all()}
    print BlogPost.objects.all()
    return render(request, 'all_blog_posts.html', data)


# Returns a webpage listing a specific author's BlogPosts
def author(request, author_id):
    # Find author matching author_id or raise an HTTP 404 error
    author = get_object_or_404(Author, id=author_id)
    posts = BlogPost.objects.filter(author=author)

    data = {
        'author': author,
        'posts': posts
    }

    return render(request, 'author.html', data)


# Returns a webpage listing all authors in the database
def all_authors(request):
    # Find all authors
    data = {'authors': Author.objects.all()}
    return render(request, 'all_authors.html', data)
