# fc-list

> List available fonts installed on the system.
> More information: <https://manned.org/fc-list>.

- Return a list of installed fonts:

`fc-list`

- Return a list of installed fonts with given name:

`fc-list | grep '{{DejaVu Serif}}'`

- Return the number of installed fonts:

`fc-list | wc {{[-l|--lines]}}`

- Return a list of installed fonts that support the language based on its locale code:

`fc-list :lang={{jp}}`

- Return a list of installed fonts that contain the glyph specified by its Unicode code-point:

`fc-list :charset={{f303}}`
