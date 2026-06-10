# ocrmypdf

> Ստեղծեք որոնելի PDF կամ PDF/A սկանավորված PDF-ից կամ տեքստի պատկերից:.
> Լրացուցիչ տեղեկություններ. <https://ocrmypdf.readthedocs.io/en/latest/cookbook.html>:.

- Ստեղծեք նոր որոնելի PDF/A ֆայլ սկանավորված PDF-ից կամ պատկերային ֆայլից.:

`ocrmypdf {{path/to/input}} {{path/to/output.pdf}}`

- Բաց թողնել խառը ձևաչափով մուտքագրված PDF ֆայլի էջերը, որոնք արդեն պարունակում են տեքստ.:

`ocrmypdf --skip-text {{path/to/input.pdf}} {{path/to/output.pdf}}`

- Մաքրել, թեքել և պտտել վատ սկանավորման էջերը.:

`ocrmypdf --clean --deskew --rotate-pages {{path/to/input.pdf}} {{path/to/output.pdf}}`

- Կատարեք կորստի օպտիմիզացում PDF-ի վրա՝ առանց որևէ OCR կատարելու.:

`ocrmypdf --tesseract-timeout 0 --optimize 2 --skip-text {{path/to/input.pdf}} {{path/to/output.pdf}}`

- Սահմանեք որոնելի PDF ֆայլի մետատվյալները.:

`ocrmypdf --title "{{title}}" --author "{{author}}" --subject "{{subject}}" --keywords "{{keyword; key phrase; ...}}" {{path/to/input.pdf}} {{path/to/output.pdf}}`

- Ցուցադրել օգնությունը.:

`ocrmypdf --help`
