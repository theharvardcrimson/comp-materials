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

```yaml
layout: 'two-cols'
```

```html
<div id="author" />

<script>
  document.getElementById('author')
  document.querySelector('#author')
  document.querySelectorAll('#author')[0]

  const timer = setTimeout(() => {})
</script>
```

---

# Consult MDN

- https://developer.mozilla.org/en-US/docs/Web/JavaScript
