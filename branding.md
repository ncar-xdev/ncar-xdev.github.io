# Branding

Below are the logos, icons, and specifications needed to reproduce the Xdev brand in your own documents, slides, etc.

## Logos

::::{panels}

---

For dark themes
^^^^^^^^^^^^^^^

:::{image} images/xdev_logo_light.svg
:alt: xdevlight
:class: bg-dark
:::

---

For light themes
^^^^^^^^^^^^^^^^

:::{image} images/xdev_logo_dark.svg
:alt: xdevdark
:class: bg-light
:::

::::

## Icons

::::{panels}

---

For dark themes
^^^^^^^^^^^^^^^

:::{image} images/x_icon_light.png
:alt: xlight
:align: center
:width: 50px
:::

---

For light themes
^^^^^^^^^^^^^^^^

:::{image} images/x_icon_dark.png
:alt: xdark
:align: center
:width: 50px
:::

::::

## Specification

The `X` in the Xdev logo is written with an uppercase "X" in the Google Font
[Saira Stencil One](https://fonts.google.com/specimen/Saira+Stencil+One).
The `dev` in the Xdev logo is written with lowercase "dev" in the Google Font
[Audiowide](https://fonts.google.com/specimen/Audiowide?query=audiowide).
Both fonts should have the same `font-size` and `font-weight: 400;` (or the
default `font-weight`).

The logo can be reproduced in HTML with inclusion of the appropriate Google
Font stylesheets in the `<head>...</head>` section:

```html
<link href="https://fonts.googleapis.com/css?family=Saira+Stencil+One&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css?family=Audiowide&display=swap" rel="stylesheet">
```

afterwhich elements in your HTML can be specify fonts with the appropriate styles:

```css
font-family: 'Audiowide';
```

or

```css
font-family: 'Saira Stencil One';
```
(Note that with HTML5, you can place the `<link ...>` tags above directly in the body,
which is what makes the below example work.)

This allows you to write the Xdev logo purely with text like so:

```html
<style>
  span.xdev-x {
    font-family: 'Saira Stencil One';
  }
  span.xdev-dev {
    font-family: 'Audiowide';
  }
</style>
<span class="xdev-x">X</span><span class="xdev-dev">dev</span>
```

which should display like <span style="font-family: 'Saira Stencil One'">X</span><span style="font-family: 'Audiowide';">dev</span>.
