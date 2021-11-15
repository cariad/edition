---
author: Cariad Eccleston
favicon-emoji: 📰
title: Edition
---

# 📰 Edition

**WARNING: This is a pre-release project.**

**Edition** is a command-line application for creating beautiful HTML and Markdown editions of your projects' documentation.

In fact, the document you're reading right now was pressed by Edition.

<edition value="toc" />

## ✨ Highlights

- **Write your documentation once.**<br />Edition will give you an `README.md` to upload to your project, PyPI and all the rest, _and_ a beautiful HTML page ready to upload directly to GitHub or GitLab Pages.
- **Works out of the box.**<br />With one command, your existing `README.md` can be converted to beautiful HTML.
- **Embed your code samples.**<br />Edition will execute your code and embed the results.

## ✋ Example

Create this Markdown document named `example-source.md`:

~~~markdown
# Edition example

Save this file to your local machine as `example-source.md`
then run:

```bash
edition example-source.md example.html --press html
```

Now open `example.html` in a web browser. The code example
below will be complete.

```bash
python --version
```

<!--edition-exec-->
~~~

Run:

```bash
python -m edition docs/example-source.md docs/example.html --press html
```

<!--edition-exec-->

This will generate [example.html](example.html). Open that file in a web browser.

## 🤔 Is Edition right for you?

Edition could be great for you if:

- You've tried other documentation tools and they were more complex or time-consuming than you care for
- Your documentation fits on a single page

Edition is not a feature-matching substitute for Sphinx, mkdocs, pdoc or the like, nor is Edition aiming to be.

If you need multi-page documentation, docstring parsing or fine configuration then Edition is not right for you.

## ⚙️ Getting Started

Edition requires **Python 3.8** or later.

Install Edition via `pip`:

```bash
pip install edition
```

## 📄 Creating your source document

Your **source document** is the Markdown document from which all your editions will be pressed.

Any Markdown document you already have -- like your project's `README.md` -- is already a valid source document, but we can add some front matter and additional markup to help guide the presses.

### Front matter

The following front matter properties come into play only when pressing HTML.

| Property      | Description             | Default           |
| :------------ | :---------------------- | :---------------- |
| author        | Author name             | No author         |
| favicon-emoji | Emoji to use as favicon | No favicon        |
| title         | Page title              | Top-level heading |

For example:

```markdown
---
author: Cariad Eccleston
favicon-emoji: 🍕
# If "title" was omitted then the top-level "Example"
# heading would be used instead:
title: Embedded Example

---
# Example
```

### Markup

#### Code execution

To have Edition execute your code then embed the result:

1. Create a regular Markdown code block
1. Add `<!--edition-exec-->` after the block

For example:

~~~markdown
```python
print("Hello, world!")
```

<!--edition-exec-->
~~~

Currently only `bash` and `python` code blocks are supported. More languages can be added if they are [requested](#contributing).

#### Table of Contents

```html
<edition value="toc" />
```

## 🍰 Contributing

Thank you for considering contribution!

To contribute a bug report, enhancement or feature request, please raise an issue at [github.com/cariad/edition/issues](https://github.com/cariad/edition/issues).

If you want to contribute a code change, please raise an issue first so we can chat about the direction you want to take.

## 👮‍♀️ Licence

Edition is released at [github.com/cariad/edition](https://github.com/cariad/edition) under the MIT Licence.

See [LICENSE](https://github.com/cariad/edition/blob/main/LICENSE) for more information.

## 👩‍💻 The Author

Hello! 👋 I'm **Cariad Eccleston** and I'm a freelance DevOps and backend engineer. My contact details are available on my personal wiki at [cariad.earth](https://cariad.earth).

Please consider supporting my open source projects by [sponsoring me on GitHub](https://github.com/sponsors/cariad/).

## 🔗 Related Projects

- Epic thanks to John Gruber for releasing the [Markdown specification](https://daringfireball.net/projects/markdown/).
