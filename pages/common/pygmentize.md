# pygmentize

> Python-based syntax highlighter.

- Highlight file syntax and print to standard output (language is inferred from the file extension):

`pygmentize {{file.py}}`

- Highlight syntax for a given language:

`pygmentize -l {{javascript}} {{input_file}}`

- List avaliable lexers (processors for input languages):

`pygmentize -L lexers`

- Save output to a file in HTML format:

`pygmentize -f html -o {{output_file.html}} {{input_file.py}}`

- List avaliable output formats:

`pygmentize -L formatters`

- Output to HTML file with line numbers:

`pygmentize -f html -O linenos=1 -o {{output_file.html}} {{input_file}}`
