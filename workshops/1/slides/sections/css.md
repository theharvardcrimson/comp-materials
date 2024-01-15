```yaml
layout: "statement"
```

# CSS

---

```yaml
layout: "two-cols"
```

```html
<div id="author"></div>
```

- No two elements can share an `id`
- Meant for selecting with JS or unique, important elements

<br />

```html
<div class="card">Card 1</div>
<div class="card">Card 2</div>
```

- Meant for reusable styles

<div class="grid grid-cols-2 gap-sm mt-4">
  <div class="rounded-md bg-gray text-black px-2">Card 1</div>
  <div class="rounded-md bg-gray text-black px-2">Card 2</div>
</div>

::right::

<div class="ml-8" v-click>

```css
#author {
  font-size: 1.125rem;
}

.card {
  border-radius: 0.375rem;
  background-color: gray;
}
```

</div>

---

# Customization

- Anything you can almost imagine
- `color`, `transition`, `background-image`, etc.

<v-clicks depth="2">

- Explore using [MDN on CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- Experiment with LLMs using _specific_ and _fundamental_ prompts that is based off of CSS properties
  - <span class="bg-green-600 px-1">Good</span>: "Give CSS for a `div` that is rounded, can be positioned anywhere, and has a shadow"
    - Will give the right values for the necessary properties
  - <span class="bg-red-600 px-1">Bad</span>: "Give CSS for a beautiful alert element"
    - More likely to give copied code from a repo with unclear licensing
    - Is not aware of codebase readability and best practices

</v-clicks>

---

# Consult MDN

- https://developer.mozilla.org/en-US/docs/Web/CSS
