# text-fmt

> Ձևաչափել LaTeX աղբյուրի կոդը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/WGUNDERWOOD/tex-fmt>:.

- Ձևաչափեք ֆայլը՝ վերագրանցելով բնօրինակը.:

`tex-fmt {{path/to/file.tex}}`

- Ստուգեք, արդյոք ֆայլը ճիշտ ձևաչափված է.:

`tex-fmt --check {{path/to/file.tex}}`

- Ձևաչափեք `stdin`-ից կարդացված ֆայլը և տպեք `stdout`:

`cat {{path/to/file.tex}} | tex-fmt --stdin`
