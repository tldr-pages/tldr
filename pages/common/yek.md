# yek

> Serialize a repository or directory into an LLM-friendly single file (fast Rust-based repomapper).
> More information: <https://github.com/bodo-run/yek>.

- Serialize the current directory and write the output to a temp file (prints path):

`yek`

- Serialize specific directories and write output to a directory:

`yek {{src/}} {{tests/}} --output-dir {{/tmp/yek}}`

- Process multiple files or use glob patterns (quote globs to avoid shell expansion):

`yek "{{src/**/*.rs}}" "{{docs/**/*.md}}"`

- Cap the token-based output size to 128k tokens:

`yek {{src/}} --tokens {{128k}}`

- Cap the byte-based max output size and set an explicit output file name:

`yek {{src/}} --max-size {{100KB}} --output-name {{yek-output.txt}}`

- Stream JSON output:

`yek {{src/}} --json`

- Include a directory tree header in the output:

`yek {{src/}} --tree-header`
