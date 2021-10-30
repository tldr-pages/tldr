# figlet

> Generate ASCII banners from user input.
> See also: `showfigfonts`.
> More information: <http://www.figlet.org/figlet-man.html>.

- Generate by directly inputting text:

`figlet {{input_text}}`

- Use a custom font file:

`figlet {{input_text}} -f {{path/to/font_file.flf}}`

- Use a font from the default font directory (the extension can be omitted):

`figlet {{input_text}} -f {{font_filename}}`

- Pipe command output through FIGlet:

`{{command}} | figlet`

- Show available FIGlet fonts:

`showfigfonts {{optional_string_to_display}}`
