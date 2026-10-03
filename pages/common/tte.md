# tte

> A terminal visual effects engine, application, and library.
> More information: <https://github.com/ChrisBuilds/terminaltexteffects>.

- Apply a random effect to a command's output:

`{{command}} | tte --random-effect`

- Apply a specific effect to a command's output:

`{{ls -la}} | tte {{matrix}}`

- View the options for a specific effect:

`tte {{decrypt}} -h`

- Apply an effect to text from a file:

`tte --input-file {{path/to/file}} {{beams}}`

- Print shell completion scripts:

`tte --print-completion {{bash}}`
