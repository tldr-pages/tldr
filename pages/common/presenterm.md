# presenterm

> A terminal-based slideshow tool that renders markdown presentations.
> More information: <https://github.com/mfontanini/presenterm>.

- Display a presentation:

`presenterm {{path/to/slides.md}}`

- Display a presentation with a specific theme:

`presenterm --theme {{dark|light|tokyonight-storm|...}} {{path/to/slides.md}}`

- List all available themes:

`presenterm --list-themes`

- Export a presentation to PDF:

`presenterm --export-pdf --output {{path/to/output.pdf}} {{path/to/slides.md}}`

- Display a presentation with code snippet execution enabled:

`presenterm --enable-snippet-execution {{path/to/slides.md}}`

- Validate that presentation content fits within the terminal:

`presenterm --validate-overflows {{path/to/slides.md}}`
