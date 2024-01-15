## Introduction

This is a project that should only involve HTML, CSS, JS without any external dependencies.

### Pages

| Page               | Description                                                                                                                                                             |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `index.html`       | "Home" page that gives a basic structure as a reminder.                                                                                                                 |
| `about.html`       | "About" page that should contain two links to its subpages.                                                                                                             |
| `about/me.html`    | "About Me" page that contains a short description about you.                                                                                                            |
| `about/modal.html` | "About Modal" page that contains a button that once clicked should open a [modal](https://uxplanet.org/best-practices-for-modals-overlays-dialog-windows-c00c66cddd8c). |

All pages are blank except for the starter code in `index.html`.

## Todo

Try your best to debug and struggle through without relying on ChatGPT or direct help from others (i.e. resources that just away the answer). The end goal is for you to be able to conceptualize how sites fundamentally work, not testing you!

- Fill all pages with the correct content.
- `about/modal.html` contains a button that should open the modal by executing JS. Instead of using its `onclick` attribute, use an [event listener](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener).
- Modal should meet the below specification.
  - The modal should not exist in DOM (not simply just hidden with CSS) until the "open" button is clicked.
  - The modal should be completely removed from DOM when the "close" button is clicked.
  - The modal should have a width and height of `20rem` and be centered in the screen.

## Hints

- If a `div` only contains text, consider using a `p` paragraph element. But `p` should not contain anything other than text.
- Try reading on `document.getElementById('modal').innerHTML` or, alternatively, [templates](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/template).
- For the modal positioning, read up on [absolute and relative positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/position) and using [flexbox alignment](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_flexible_box_layout/Aligning_items_in_a_flex_container). Then, try to explore how to use multiple `div`s to make the systems work.
