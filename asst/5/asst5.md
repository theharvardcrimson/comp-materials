# Assignment 5 - Moar Django

We're back! As always, feel free to email Jessica (jessica.zhu@thecrimson.com) or Kyle (kyle.kwong@thecrimson.com) if you have any questions!

## Plan of Attack
Remember this?

![turnip](http://i.giphy.com/X0YkzoS6UqVfa.gif)

JK don't be aggressive. Unless someone is being as bratty as [Mertle Edmonds](http://disney.wikia.com/wiki/Mertle_Edmonds). Then crush them.

1. Use the admin interface.
2. Make pages for Articles (html and views).
3. Make a homepage (html).
4. Edit the admin form for Articles to, instead of having a textField, to have a TinyMCE field.
5. Make a migration :o.

You finished 1-3 last week in one piece (hopefully), and this week we're going to tackle the last two TODOs!


## Customize the Article Admin
This part is tricky because it involves reading documentation (gasp!). The idea is to figure out how to plug in TinyMCE into the admin interface so that users can input formatted content (bolding, italicizing, and underlining - OH MY.)

Resources:

- A helpful page on how to change the elements on the admin interface is located [here](https://docs.djangoproject.com/en/1.8/intro/tutorial02/#customize-the-admin-form).
- TinyMCE installation instructions here (be sure to `workon` your virtual environment!).
- ... and documentation on how to use it is [here](http://django-tinymce.readthedocs.org/en/latest/usage.html). Go nuts!

Don't worry if it seems nebulous - it may be helpful to work with another tech comper on this, so refer to the facecard wall, or ask us if you hit a wall.

## Make a Migration
Add one field of your choice to any of the `content` models, and make a migration! To do this, we must execute four steps.

1. Make a change to your models! Like add a field or something. Migrations are boring if there's nothing to migrate :D
2. Create the migration file "automagically" (bleh!) via Django's built-in migration system.

        ./manage.py makemigrations <app_name>
3. Optional: Check to see the migration is there in the migrations folder. Maybe take a peek inside to see what Django actually did.

        ls <app_name>/migrations
4. Run the migration.

        ./manage.py migrate <app_name>

Let us know what field you added in the `README.txt` from before.

## Make it beautiful
Flex those HTML/CSS/JS muscles and make your website (or at least one page of it) beautiful. Or terrible. Just write some HTML, CSS, and maybe some JavaScript.

## Huzzah!
Congrats! Now you know how to Django. (If you say it fast enough, people might even think you know how to dance!) Push your changes and rejoice!
