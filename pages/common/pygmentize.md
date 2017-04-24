# pygmentize

> Python based syntax highlighter.

- Highlight file syntax and print to standard output. Language is inferred from the file extension:

`pygmentize {{file.py}}`

- Highlight syntax for a given language:

`pygmentize -l {{javascript}} {{javascript_file}}`

- Show avaliable lexers:

`pygmentize -L lexers`

- Save output to a file in HTML format:

`pygmentize -f html -o {{file.html}} {{file.py}}`

- Show avaliable output formats:

`pygmentize -L formatters`

- Output to HTML file with line numbers, specifying a given language:

`pygmentize -f html -O linenos=1 -l {{language}} -o {{file.html}} {{file}}`
