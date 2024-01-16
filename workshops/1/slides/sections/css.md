```yaml
layout: 'statement'
```

# CSS

---

```yaml
layout: 'two-cols'
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

# `px` vs. `rem`

<v-clicks depth="2">

- `px` are pixels that you are familiar with, like making your essay have font size `12`
- `rem` is relative
  - Why is this important for the web? Web needs to be universally accessible, so when people that set their system to use larger font sizes, sites should resize everything as well.
  - Selected font size (default `16px`) times `rem` value is ultimate size.
  - Scale all sizes like width, margin, etc. with `rem`, not just fonts

</v-clicks>

---

```yaml
layout: 'two-cols-header'
```

# Horizontal Centering

::left::

```html
<div>
  Lorem ipsum dolor sit amet, qui minim labore
  <a>anchor tag (link)</a>
  minim sint cillum sint consectetur cupidatat.
  <div class="bg-black" />
  Lorem ipsum dolor sit amet
</div>
```

::right::

<div v-click="[0, 1]">

#### `text-align: center`

<div class="text-center bg-gray w-full p-1 my-2">
Lorem ipsum dolor sit amet, qui minim labore <a href="https://thecrimson.com" target="_blank">anchor tag (link)</a> minim sint cillum sint consectetur cupidatat.
<div class="bg-black h-6" />
Lorem ipsum dolor sit amet
</div>

- Only `inline` elements center because `block` elements fill width anyways

</div>

<div class="absolute top-0" v-click>

#### `flex: 1; justify-content: center`

<div class="flex justify-center bg-gray w-full p-1 gap-2 my-2">
Lorem ipsum dolor sit amet, qui minim labore <a class href="https://thecrimson.com" target="_blank">anchor tag (link)</a> minim sint cillum sint consectetur cupidatat.
<div class="bg-black w-6" />
Lorem ipsum dolor sit amet
</div>

- All elements are coerced into `block`

</div>

---

# Vertical Centering

- Must use `flex: 1; align-items: center`

<div class="flex items-center bg-gray w-1/2 h-1/2 p-1 mt-4">
  <div>
    <div class="h-10 w-10 bg-black" />
  </div>
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
