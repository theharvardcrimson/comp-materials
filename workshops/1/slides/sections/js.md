```yaml
layout: 'section'
```

# JS

---

# What Is It?

- Runs in your browser along with HTML and CSS or independently on `node` (unimportant for now)
- Dynamically typed, i.e. `let a = 3; a = 'string'` is valid
- When using with HTML, put JS in `script` tags

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

```yaml
layout: 'two-cols'
```

# If-Else and Ternary Operator

```js
let a
if (true) {
  a = 1
} else {
  a = 2
}
```

The above is equivalent to the following.

```js
let a = true ? 1 : 2
```

::right::

- `0`, `''`, `null`, `undefined`, `NaN` are equivalent to `false`; otherwise, value is truthy
- Just syntactic sugar; neither is more efficient than the other
- Use either depending on situation for best readability

---

# Switch

- Can be better for readability than a long if-else sequence
- Note the scoping per case

```js
const userInput = 'maybe'
switch (userInput) {
  case 'yes': {
    console.log('Thanks for buying!')
    break
  }
  case 'no': {
    console.log("We hope you'll buy next time.")
    break
  }
  case 'maybe': {
    console.log('We put it on your wishlist!')
    break
  }
  default: {
    console.log('Invalid input. Please try again.')
    break
  }
}
```

---

# Loops

```js
while (false) {
  console.log('The Crimson')
}

do {
  console.log('The Crimson')
} while (false)

for (let i = 0; i < 10; ++i) {
  console.log(i)
}
```

---

# `undefined` vs. `null`

- `undefined` only has meaning for the programmer
- `null` should have meaning for the data a variable holds

---

# Functions

- camelCase by convention
- Similar to Python preferring snake_case
- `restArgs` is an array of 0 or more arguments

```js
function name(arg1, arg2, ...restArgs) {
  // Code
}
```

```js
const name = (arg1, arg2, ...restArgs) => {
  // Code
}
```

---

# Objects

- Essentially equivalent to JS Object Notation (JSON)
- Holds key-value pairs

```js
const userProfile = {
  fullName: 'Dennis Eum',
  password: 'crimson',
  security: [
    {
      question: 'Favorite color?',
      answer: '#1a1b26',
    },
  ],
}
```

---

# Comparison

- `>`, `>=`, `<`, `<=`
- Use `===` and `!==`, which is strict
- There exists `==` and `!=` that allow comparisons between different types, but **never** use

```js
console.log('' == '0') // `false`
console.log(0 == '') // `true`
console.log(0 == '0') // `true`

console.log(false == 'false') // `false`
console.log(false == '0') // `true`
```

---

```yaml
layout: 'two-cols'
```

# Call-By-Sharing

```js
function change(arg1, arg2, arg3) {
  ++arg1
  arg2 = { crimson: true }
  arg3.crimson = true
}

let a = 0
let b = { crimson: false }
let c = { crimson: false }

change(a, b, c)
```

::right::

<v-click>

```js
console.assert(a === 0)
console.assert(b.crimson === true)
console.assert(c.crimson === false)
```

</v-click>

---

```html
<div id="author" />

<script>
  const authorEl = document.getElementById('author')
</script>
```

```js
console.log('')
```

---

# Consult MDN

- https://developer.mozilla.org/en-US/docs/Web/JavaScript
