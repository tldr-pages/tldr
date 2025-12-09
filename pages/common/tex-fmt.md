# tex-fmt

> Format LaTeX source code.
> More information: <https://github.com/WGUNDERWOOD/tex-fmt>.

- Format a file, overwriting the original:

`tex-fmt {{path/to/file.tex}}`

- Check if a file is correctly formatted:

`tex-fmt --check {{path/to/file.tex}}`

- Format a file read from `stdin` and print to `stdout`:

`cat {{path/to/file.tex}} | tex-fmt --stdin`
