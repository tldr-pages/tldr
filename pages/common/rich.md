# rich

> Rich CLI - fancy terminal display.
> More information: <https://github.com/Textualize/rich-cli>.

- Show file contents with syntax highlighting:

`rich file.py`

- Add line numbers, and indentation guides:

`rich file.py --line-number --guides`

- Apply a theme:

`rich file.py --theme monokai`

- Display file in an interactive pager:

`rich file.py --pager`

- Display contents from a URL:

`rich https://raw.githubusercontent.com/Textualize/rich-cli/main/README.md --markdown --pager`

- Export a file as HTML:

`rich file.md -o file.html`

- Print text with formatting tags, custom alignment, and fixed line width:

`rich --print "Hello [green on black]Stylized[/green on black] [bold]World[/bold]" --center --width 10`
