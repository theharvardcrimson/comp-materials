## Introduction

You are building a task app where you can create, delete, and complete a task.

### Create

- At the bottom of the task list, there is an input and a button (side by side).
- If there is no text in the input, the button does nothing. Otherwise, the button will clear the input and add the task to the task list. 

### Delete

- The task should be deleted from the task list.

### Complete

The implementation should be the same as deleting a task except:

- Clicking on a task should display an alert `div` on the bottom of the page with the text "Complete."
- The alert should be removed from the DOM (i.e. unrender itself) after 2 seconds.

## Explore

1. Updating the array of tasks rerenders all tasks. Instead, make only the specific task affected by an action rerender/update? If unsure, use the profiler in the React browser extension to observe which components rerender.



