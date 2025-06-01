# markdown2pdf

> Markdown2pdf is a simple commandline tool to convert markdown to PDF.
> More information: <https://github.com/theiskaa/markdown2pdf>.

- Convert any .md file regardless of name to a output.pdf:

`markdown2pdf -p "path/to/file.md"`

- Convert .md file to a .pdf file of a specified path and name:

`markdown2pdf -p "path/to/file.md" -o "different/path/to/file/pdf"`

- Convert Markdown content provided as a string:

`markdown2pdf -s "**bold text** *italic text*." -o "string.pdf"`

- Convert from URL (this will convert README.md at that URL to local readme.pdf):

`markdown2pdf -u "https://raw.githubusercontent.com/user/repo/main/README.md" -o "readme.pdf"`
