# texcount

> Count words in TeX documents omitting macros.
> Note: if the TeX document uses `\include` or `\input` and you want to count the included files, `texcount` must be run in the directory of the root TeX file.
> More information: <https://app.uio.no/ifi/texcount/howto.html>.

- Count words in a TeX file:

`texcount {{path/to/file.tex}}`

- Count words in a document and subdocuments built with `\input` or `\include`:

`texcount -merge {{file.tex}}`

- Count words in a document and subdocuments, listing each file separately (and a total count):

`texcount -inc {{file.tex}}`

- Count words in a document and subdocuments, producing subcounts by chapter (instead of subsection):

`texcount -merge -sub=chapter {{file.tex}}`

- Count words with verbose output:

`texcount -v {{path/to/file.tex}}`
