# rich

> Rich CLI - fancy terminal display.
> More information: <https://github.com/Textualize/rich-cli>.

- Display a specific file with syntax highlighting:

`rich {{path/to/file.py}}`

- Add line numbers, and indentation guides:

`rich {{path/to/file.py}} --line-number --guides`

- Apply a specific theme:

`rich {{path/to/file.py}} --theme {{monokai}}`

- Display a specific file in an interactive pager:

`rich {{path/to/file.py}} --pager`

- Display contents from a specific URL:

`rich {{https://raw.githubusercontent.com/Textualize/rich-cli/main/README.md}} --markdown --pager`

- Export a file as HTML:

`rich {{path/to/file.md}} -o {{path/to/file.html}}`

- Print text with formatting tags, custom alignment, and fixed line width:

`rich --print {{"Hello [green on black]Stylized[/green on black] [bold]World[/bold]"}} --center --width {{10}}`
