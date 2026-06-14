# cmark

> Փոխարկել CommonMark Markdown ձևաչափված տեքստը այլ ձևաչափերի:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/cmark>:.

- Ներկայացրեք CommonMark Markdown ֆայլը HTML.:

`cmark --to html {{filename.md}}`

- Փոխարկել տվյալները `stdin`-ից LaTeX:

`cmark --to latex`

- Ուղղակի մեջբերումները վերածեք խելացի մեջբերումների.:

`cmark --smart --to html {{filename.md}}`

- Վավերացնել UTF-8 նիշերը.:

`cmark --validate-utf8 {{filename.md}}`
