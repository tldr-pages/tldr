# cp

> Copy files.

- Copy files in arbitrary locations:

`cp {{/path/to/original}} {{/path/to/copy}}`

- Copy a file to a parent directory:

`cp {{/path/to/original}} ../{{path/to/copy}}`

- Copy directories recursive using the option -r:

`cp -r {{/path/to/original}} {{/path/to/copy}}`

- Show files as they are copied:

`cp -vr {{/path/to/original}} {{/path/to/copy}}`

- Make a copy of a file, adding an extension:

`cp {{file.html}}{,.backup}`

- Make a copy of a file, changing the extension:

`cp {{file.}}{html,backup}`
