# mkdist

> Build package distributions while preserving individual file structure and generating TypeScript declarations.
> More information: <https://github.com/unjs/mkdist>.

- Transpile files from the source directory to the output directory:

`mkdist`

- Specify custom source and output directories:

`mkdist --src {{src}} --dist {{dist}}`

- Generate TypeScript declaration files alongside transpiled modules:

`mkdist --declaration`

- Clean the destination directory before building:

`mkdist --clean-dist`
