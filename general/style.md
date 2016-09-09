# Python Style and Design
If you're new to Python, chances are that style and design are the last things on your mind. There's a lot to remember, which is why we've assembled some basics (so you don't have to go hunt them down yourselves)!

## Style
### Basics
Comments, spacing, etc.: be practical and consistent.

### Quotation Marks
Use single quotes. Please. Except docstrings and HTML. Replace double quotes when you see them.

### Spaces
Put spaces between things (list items, binary operations, etc.).

### Line Length
80 characters.

### Indentation
Remember, this actually matters: 4 **spaces**. *SPACES NOT TABS*

### Trailing White Space
Avoid it._ <-- bad

## Design
What does "Pythonically" mean?

### Strings
Rather than concatenating strings using +, use the format function or lists.

	# Bad.
	'Hello, ' + a + ': ' + b
	# Instead:
	'Hello, {0}: {1}'.format(a, b)

	# Bad.
	for string in list:
		new string += string
	# Instead:
	''.join(list)

### Lists
List comprehensions are your friend.