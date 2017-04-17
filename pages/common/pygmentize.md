# pygmentize

> CLI Python Syntax Highlighter.

- Highlight syntax:

`pygmentize {{filename}}`

- Highlight syntax (another language):

`pygmentize -l {{lexer}} {{filename}}`

- Show avaliable lexers:

`pygmentize -L lexers`

- Output to HTML:

`pygmentize -f html -l {{lexer}} -o {{output}} {{filename}}`

- Show avaliable output formats:

`pygmentize -L formatters`

- Output to HTML with a line numbers:

`pygmentize -f html -O linenos=1 -l {{lexer}} -o {{output}} {{filename}}`
