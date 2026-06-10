# pdftotext

> Փոխարկել PDF ֆայլերը պարզ տեքստի ձևաչափի:.
> Լրացուցիչ տեղեկություններ. <https://www.xpdfreader.com/pdftotext-man.html>:.

- Փոխարկեք `filename.pdf`-ը պարզ տեքստի և տպեք այն `stdout`:

`pdftotext {{filename.pdf}} -`

- Փոխարկեք `filename.pdf`-ը պարզ տեքստի և պահեք այն որպես `filename.txt`:

`pdftotext {{filename.pdf}}`

- Փոխարկեք `filename.pdf`-ը պարզ տեքստի և պահպանեք դասավորությունը.:

`pdftotext -layout {{filename.pdf}}`

- Փոխարկեք `input.pdf`-ը պարզ տեքստի և պահեք այն որպես `output.txt`:

`pdftotext {{input.pdf}} {{output.txt}}`

- Փոխակերպեք `input.pdf`-ի 2-րդ, 3-րդ և 4-րդ էջերը պարզ տեքստի և պահեք դրանք որպես `output.txt`:

`pdftotext -f {{2}} -l {{4}} {{input.pdf}} {{output.txt}}`
