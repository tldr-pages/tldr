# catimg

> Image printing in the terminal.
> See also: `pixterm` and `chafa`.
> More information: <https://github.com/posva/catimg>.

- Print a JPEG, PNG, or GIF to the terminal:

`catimg {{path/to/input}}`

- Use doubled [r]esolution:

`catimg -r 2 {{path/to/input}}`

- Disable 24-bit color for better [t]erminal support:

`catimg -t {{path/to/input}}`

- Specify custom [w]idth or [H]eight:

`catimg {{-w|-H}} {{custom}} {{path/to/input}}`
