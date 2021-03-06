# 📰 Edition

**WARNING: This is a pre-release project.**

**Edition** is a command-line application for creating beautiful HTML and Markdown editions of your projects' documentation.

In fact, the document you're reading right now was pressed by Edition.

- [Highlights](#highlights)
- [Getting started](#getting-started)
  - [Installation](#installation)
  - [Quick-start example](#quick-start-example)
- [Usage](#usage)
  - [Command line](#command-line)
  - [Creating your source document](#creating-your-source-document)
    - [Front matter](#front-matter)
    - [Markup](#markup)
      - [Code execution](#code-execution)
      - [Table of Contents](#table-of-contents)
- [Project](#project)
  - [Contributing](#contributing)
  - [Licence](#licence)
  - [Author](#author)
  - [Acknowledgements](#acknowledgements)

## Highlights

- **Write your documentation once.**<br />Edition presses README.md and HTML documents ready to upload directly to GitHub Pages or any other static hosting, all from the same source.
- **Works out of the box.**<br />With one command, Edition converts your existing README.md to beautiful HTML: `edition README.md index.html --press html`
- **Embed your code samples.**<br />Edition executes embedded code and injects the results automatically.

## Getting started

### Installation

Edition requires **Python 3.8** or later.

Install Edition via pip:

```bash
pip install edition
```

### Quick-start example

Create this Markdown document as `example-source.md`:

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
edition docs/example-source.md docs/example.html --press html
```

<!--edition-exec as=markdown fence=backticks host=shell range=start-->

```text
Pressed: docs/example.html
```

<!--edition-exec range=end-->

Fun fact! The code above is executed every time I press this documentation. That gives me confidence that it works and lets you see the actual [example.html](https://cariad.github.io/edition/example.html) it generates.

## Usage

### Command line

Edition takes three command line arguments:

- Source file
- Destination file
- `--press html` to press HTML or `--press markdown` to press Markdown

### Creating your source document

Your **source document** is the Markdown document from which all your editions will be pressed.

Any Markdown document you already have -- like your project's `README.md` -- is already a valid source document, but we can add some front matter and additional markup to help guide the presses.

#### Front matter

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

#### Markup

##### Code execution

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

If your code fails then an error message will be injected:

```python
print(foo)
```

<!--edition-exec as=markdown fence=backticks host=shell range=start-->

```text
Traceback (most recent call last):
  File "<string>", line 1, in <module>
NameError: name 'foo' is not defined
```

<!--edition-exec range=end-->

Currently only `bash` and `python` code blocks are supported. More languages can be added if they are [requested](#contributing).

##### Table of Contents

To insert a table of contents:

```html
<edition value="toc" />
```

You can optionally specify "hi" and "lo" values to restrict the table to a range of headings.

For example, to exclude the title and start at second-level headings:

```html
<edition value="toc" hi="2" />
```

To exclude any headings below level three:

```html
<edition value="toc" lo="2" />
```

## Project

### Contributing

To contribute a bug report, enhancement or feature request, please raise an issue at [github.com/cariad/edition/issues](https://github.com/cariad/edition/issues).

If you want to contribute a code change, please raise an issue first so we can chat about the direction you want to take.

### Licence

Edition is released at [github.com/cariad/edition](https://github.com/cariad/edition) under the MIT Licence.

See [LICENSE](https://github.com/cariad/edition/blob/main/LICENSE) for more information.

### Author

Hello! 👋 I'm **Cariad Eccleston** and I'm a freelance DevOps and backend engineer. My contact details are available on my personal wiki at [cariad.earth](https://cariad.earth).

Please consider supporting my open source projects by [sponsoring me on GitHub](https://github.com/sponsors/cariad/).

### Acknowledgements

- The beautiful [Dracula for Pygments theme](https://github.com/dracula/pygments) is copyright of Dracula Theme and used under the MIT licence.
- Epic thanks to John Gruber for releasing the [Markdown specification](https://daringfireball.net/projects/markdown/).
- Code injection is performed by [dinject](https://github.com/cariad/dinject), copyright of Cariad Eccleston and used under the MIT licence.
