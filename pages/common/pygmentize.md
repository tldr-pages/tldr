# pygmentize

> Python-based syntax highlighter.
> More information: <https://pygments.org/docs/cmdline/>.

- Highlight file syntax and print to standard output (language is inferred from the file extension):

`pygmentize {{path/to/file.py}}`

- Explicitly set the language for syntax highlighting:

`pygmentize -l {{javascript}} {{path/to/file}}`

- List available lexers (processors for input languages):

`pygmentize -L lexers`

- Save output to a file in HTML format:

`pygmentize -f html -o {{path/to/file.html}} {{path/to/file.py}}`

- List available output formats:

`pygmentize -L formatters`

- Output an HTML file, with additional formatter options (full page, with line numbers):

`pygmentize -f html -O "full,linenos=True" -o {{path/to/file.html}} {{path/to/file}}`
