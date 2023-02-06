# pdfxup

> N-up PDF oldalak. Az N-up több oldal egy oldalra helyezését jelenti, méretezéssel és elforgatással, rácsba rendezéssel. További információ: <https://ctan.org/pkg/pdfxup>.

- 2-up PDF létrehozása:

`pdfxup -o {{path/to/output.pdf}} {{path/to/input.pdf}}`

- PDF létrehozása 3 oszlopos és oldalanként 2 soros PDF-ben:

`pdfxup -x {{3}} -y {{2}} -o {{path/to/output.pdf}} {{path/to/input.pdf}}`

- PDF létrehozása füzet üzemmódban (2-up, és az oldalak összehajtva könyvvé rendeződnek):

`pdfxup -b -o {{path/to/output.pdf}} {{path/to/input.pdf}}`
