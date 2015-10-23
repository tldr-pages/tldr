# cp

> Copy files

- Copy files in arbitrary locations

`cp {{/path/to/original}} {{/path/to/copy}}`

- Copy a file to a parent directory

`cp {{/path/to/original}} ../{{/path/to/copy}}`

- Copy directories recursive using the option -r. Optionally showing files as they are copied.

`cp -r {{/path/to/original}} {{/path/to/copy}}`
`cp -vr {{/path/to/original}} {{/path/to/copy}}`

- Make a copy of a file adding and extension or changing an extension

`cp {{file.html}}\{,.backup\}`
`cp file.\{html,backup\}`
