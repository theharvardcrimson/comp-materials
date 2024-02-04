# comp

## Setup

### Git

This is likely already installed unless you are using [Windows](https://git-scm.com/download/win). `git` is crucial! It is your best friend.

The most common workflow might be:

- `git clone <repository>`. Most likely, you are taking a remote repository and cloning it locally to your computer.
- `git add <file>`. This stages a file, adding to the group of changes that will form a commit.
- `git commit -m <message>`. This takes the staged changes and creates a single commit (locally).
- `git push`. You take any local commits and push them to the remote repository.

### Editor

Some good editors include:

- [VS Code](https://code.visualstudio.com/) (recommended)
- [Sublime Text](https://www.sublimetext.com/) (historically popular)
- [Neovim](neovim.io) (extremely steep learning curve)

For the rest of the setup, we will assume VS Code as your IDE, but the instructions are generally applicable.

### Plugins

These are required to keep code maintanable.

- **ESLint** by Microsoft. This is a linter, which is used to flag common errors and follow rules. For example, it might flag unused variables that clutter the codebase.
- **Prettier** by Prettier. This is a formatter, which keeps every user's code to the same style to keep the codebase readable.

The following are optional but helpful during development.

- **PostCSS Language Support** by csstools.
- **Tailwind CSS IntelliSense** by Tailwind Labs.

### Node

This is what runs JavaScript and allows you to create web apps.

1. Install Volta using these [instructions](https://docs.volta.sh/guide/getting-started).
2. Run `volta install node`.

Check that `node --version` returns some version number.

Volta is a version manager that will allow the entire team to work without conflicts.

## Project

If you are already very experienced working with HTML, JS, CSS, React, etc., let us know before the first workshop. You do not have to attend the workshops if this is the case. You will, however, be asked to do extra tasks for the project.

Do not choose this option if you have used JS, React but are not familiar with:

- HTML, CSS, JS without React
- React state management and when to prefer `useState` over declaring a constant variable
- React's lifecycle and when rendering updates are triggered
- you want to better understand fundamentals of web
