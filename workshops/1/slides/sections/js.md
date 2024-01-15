```yaml
layout: 'statement'
```

# JS

---

```yaml
layout: 'two-cols'
```

```html
<!doctype html>
<html>
  <head>
    <!-- Head Content -->
  </head>
  <body>
    <!-- Body Content -->

    <script>
      // JavaScript
    </script>
  </body>
</html>
```

::right::

### Why put `script` tags at end of `body`?

<v-click>

Otherwise, loading JavaScript blocks processing and rendering all the HTML and CSS.

(Simplified analysis but suffices for now.)

</v-click>

---

```html
<div id="author" />

<script>
  const authorEl = document.getElementById('author')
</script>
```

---

```html
<div id="author" />

<script>
  // All return the same element
  document.getElementById('author')
  document.querySelector('#author')
  document.querySelectorAll('#author')[0]

  // Global/function scoped; never use this
  var a = 1

  // Block scoped
  {
    let b = 2
    console.log(b) // Logs `2` to console
  }
  console.log(b) // Gives `Uncaught ReferenceError`
</script>
```

---

# Consult MDN

- https://developer.mozilla.org/en-US/docs/Web/JavaScript
