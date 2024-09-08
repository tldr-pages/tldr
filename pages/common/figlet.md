# figlet

> Generate ASCII banners from user input.
> See also: `showfigfonts`.
> More information: <http://www.figlet.org/figlet-man.html>.

- Generate by directly inputting text:

`figlet {{input_text}}`

- Use a custom [f]ont file:

`figlet {{input_text}} -f {{path/to/font_file.flf}}`

- Use a [f]ont from the default font directory (the extension can be omitted):

`figlet {{input_text}} -f {{font_filename}}`

- Pipe command output through FIGlet:

`{{command}} | figlet`

- Show available FIGlet fonts:

`showfigfonts {{optional_string_to_display}}`

- Use the full width of the [t]erminal and [c]enter the input text:

`figlet -t -c {{input_text}}`

- Display all characters at full [W]idth to avoid overlapping:

`figlet -W {{input_text}}`
