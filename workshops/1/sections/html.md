```yaml
layout: "statement"
```

# HTML

---

```yaml
layout: "two-cols-header"
```

# Elements and Attributes

::left::

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Workshop 1</tile>
    <meta name="description"
      content="Workshop 1 Example" />
    <meta name="author"
      content="Workshop 1" />
  </head>
  <body>
    <h1>Heading 1</h1>
    <h2>Heading 2</h2>
    <h3>Heading 3</h3>
    <ol>
      <li>List Item for Ordered List</li>
    </ol>
    <ul>
      <li>List Item for Unordered List</li>
    </ul>
    <button>Button</button>
    <a href="https://thecrimson.com">Anchor; Link</a>
  </body>
</html>
```

::right::

<div class="bg-gray-800 px-3 pt-1 pb-3">
  <h1 class="!font-size-6 !mb-0">Heading 1</h1>
  <h2 class="!font-size-5">Heading 2</h2>
  <h3 class="!font-size-4">Heading 3</h3>
  <ol class="list-decimal">
    <li class="font-size-3">List Item</li>
  </ol>
  <ul class="!mt-0">
    <li class="font-size-3">List Item</li>
  </ul>
  <button class="block font-size-4">Button</button>
  <a class="font-size-4" href="https://thecrimson.com" target="_blank">Anchor; Link</a>
</div>

<v-click>

Use most meaningful tag for screenreader accessibility

- `p` instead of `div` if it contains only text
- `nav` instead of `div` if it contains content for navigating site
- `ol` if list item order has meaning; otherwise `ul`

</v-click>

---

```yaml
layout: "two-cols-header"
```

# Block vs. Inline

::left::

- `div` is block while `span` is inline. Both are the most basic/simple wrapper elements.

```html
<div>
  <span>First</span>
  <span>Second</span>
</div>
<div>
  <div>First</div>
  <div>Second</div>
</div>
```

<div class="bg-gray p-4">
  <span class="bg-red">First</span>
  <span class="bg-green">Second</span>
</div>
<div class="bg-gray p-4">
  <div class="bg-red">First</div>
  <div class="bg-green">Second</div>
</div>

::right::

<div class="ml-8">

- Do not put block elements within inline ones

```html
<!-- Bad -->
<span>
  <div></div>
</span>

<!-- Okay -->
<div>
  <span>1</span>
  <span>2</span>
  <div>3</div>
</div>
```

</div>

---

- For on click, use `button` tags for JS events and `a` tags for URL objects

- Avoid using `onclick` on `a` and, instead, always use `button` for any JS

```html
<!-- Bad -->
<a onclick="alert()">Anchor</a>

<!-- Good -->
<button onclick="alert()">Button</button>
```

---

# Consult MDN

- https://developer.mozilla.org/en-US/docs/Web/HTML
