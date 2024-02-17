```yaml
colorSchema: 'dark'
highlighter: 'shiki'
layout: 'intro'
titleTemplate: '%s'
```

# Workshop 2

Javascript and TypeScript

---

# Promises

```js
fetch('https://api.thecrimson.com', {
  method: 'GET',
}) // Returns a `Promise` object
```

```js
async function getData() {
  return await fetch...
}

const getData = () => {
  return new Promise((resolve, reject) => {
    try {
      const result = await fetch...
    } catch (err) {
      reject(err)
    }
    resolve(result)
  })
}
```

---

# Dynamic vs. Static Types

- Dynamically typed languages include Python, Lua, JS

```python
age = 18 # No defined type for variable
age = "18" # No error, and that is okay!
```

- Statically typed languages include C, CPP, Rust, TS

```c
int age = 18 // Variable has a set type
age = "18" // Error! Will not even compile.

```

---

# How Does TSC Work?

- It is a compiler that compiles TS down to JS
- `tsc index.ts` $\rightarrow$ `index.js`

---

# But More Important Reason...

- New specifications for ECMAScript come out, which JS is derived from
- Browsers will never have most recent specification implemented in their JS runtime
- Thus, TS allows us to program using convenience of modern JS without worrying about compatibility

---
