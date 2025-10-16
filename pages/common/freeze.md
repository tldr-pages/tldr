# freeze

> Generate images of code and terminal output.
> Supported formats are PNG, SVG, and WebP.
> See also: `silicon`.
> More information: <https://github.com/charmbracelet/freeze#flags>.

- Generate an image of code based on a file:

`freeze {{path/to/file}}`

- Specify the output path:

`freeze {{path/to/file}} {{[-o|--output]}} {{path/to/output_image.png}}`

- Generate an image of terminal output:

`freeze {{[-x|--execute]}} {{command}}`

- Interactively customize the output image:

`freeze {{path/to/file}} {{[-i|--interactive]}}`

- Select a theme for syntax highlighting:

`freeze {{path/to/file}} {{[-t|--theme]}} {{dracula}}`

- Use a base configuration template:

`freeze {{path/to/file}} {{[-c|--config]}} {{base|full|user}}`

- Capture a specific range of line numbers:

`freeze {{path/to/file}} --lines {{start}},{{end}}`

- Show line numbers:

`freeze {{path/to/file}} --show-line-numbers`
