# Design system

Status: **not started.** Phase 1, step 1.1 owns this document.

## Existing theme pipeline (baseline)

- LESS source: `stuff/config/qss/Medium/less/`. `base/colors.less` and `base/mixins.less` define the tokens, and `themes/*.less` override them.
- The current theme variants are Medium, Dark (`@bg: #303030`), Darker (`@bg: #202020`), Light and Neutral.
- Each theme has a `// out:` header that names the generated `.qss` file. Compile it with `lessc` or the VS Code *Easy LESS* extension. See `doc/how_to_stylesheet.md`, but note that the doc's `Default/less` path is now `Medium/less`.

## To be defined in Phase 1

Colour tokens (backgrounds, surfaces, borders, accent, hover and selected states, warning and error), typography scale, spacing scale, icon sizes and states, contrast targets (WCAG AA for text), tooltips and scrollbars.
