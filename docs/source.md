---
author: Cariad Eccleston
favicon-emoji: 📰
---

# 📰 Edition

**WARNING: This is a pre-release project.**

**Edition** is a command-line application for creating beautiful HTML and Markdown editions of your projects' documentation.

In fact, the document you're reading right now was pressed by Edition.

<edition value="toc" />


## Highlights

- Write your documentation once and Edition gives you a `README.md` _and_ a beautiful HTML page ready to upload directly to GitHub Pages.
- Executes your code inside your documentation to demonstrate the results.

## Example

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

## Is Edition right for you?

Edition could be great for you if:

- You've tried other documentation tools and they were more complex or time-consuming than you care for
- Your documentation fits on a single page

Edition is not a feature-matching substitute for Sphinx, mkdocs, pdoc or the like, nor is Edition aiming to be.

If you need multi-page documentation, docstring parsing or fine configuration then Edition is not right for you.

## Getting Started

### Prerequisites

- Python 3.8 or later

### Installation

```bash
pip install edition
```

## Creating your source document

Your **source document** is the Markdown document from which all your editions will be pressed.

Any Markdown document you already have -- like your project's `README.md` -- is already a valid source document, but we can add some front matter and additional markup to help guide the presses.

### Front matter

The following front matter properties come into play only when pressing HTML.

| Property      | Description             | Default           |
| :------------ | :---------------------- | :---------------- |
| author        | Author name             | No author         |
| favicon-emoji | Emoji to use as favicon | No favicon        |
| title         | Document title          | Top-level heading |

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
