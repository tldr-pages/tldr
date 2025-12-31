# yek

> Serialize a repository or directory into an LLM-friendly single file (fast Rust-based repomapper).
> More information: <https://github.com/bodo-run/yek#usage>.

- Serialize the current directory and write the output to a temp file (prints path):

`yek`

- Serialize specific directories and write output to a directory:

`yek {{path/to/directory1 path/to/directory2 ...}} --output-dir {{path/to/output_directory}}`

- Process multiple files or use glob patterns (quote globs to avoid shell expansion):

`yek "{{path/to/directory/**/*.rs}}" "{{path/to/directory/**/*.md}}"`

- Cap the token-based output size to 128k tokens:

`yek {{path/to/directory}} --tokens 128k`

- Cap the byte-based max output size and set an explicit output file name:

`yek {{path/to/directory}} --max-size {{100KB}} --output-name {{yek-output.txt}}`

- Stream JSON output:

`yek {{path/to/directory}} --json`

- Include a directory tree header in the output:

`yek {{path/to/directory}} --tree-header`
