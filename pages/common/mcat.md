# mcat

> Parse, convert, and preview files (including Markdown), directories, images, and videos.
> More information: <https://github.com/Skardyy/mcat>.

- Display the contents of a file:

`mcat {{path/to/file}}`

- Display a Markdown file with a specific theme:

`mcat --theme {{theme_name}} {{path/to/file}}.md`

- Display an image or video inline:

`mcat --output inline {{path/to/file}}`

- Convert a file to a specific format (e.g. `html`, `md`, `image`):

`mcat --output {{format}} {{path/to/file}}`

- List the contents of a directory:

`mcat {{path/to/directory}}`

- List the contents of a directory including hidden files:

`mcat --hidden {{path/to/directory}}`

- Display content without paging:

`mcat --paging never {{path/to/file}}`
