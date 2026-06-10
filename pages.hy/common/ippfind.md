# ippfind

> Գտեք ծառայություններ, որոնք գրանցված են DNS սերվերով կամ հասանելի են տեղական սարքերի միջոցով:.
> Տես նաև՝ `ipptool`, `ippeveprinter`:.
> Լրացուցիչ տեղեկություններ. <https://openprinting.github.io/cups/doc/man-ippfind.html>:.

- Ցուցակե՛ք ցանցում գրանցված IPP տպիչները իրենց կարգավիճակով.:

`ippfind {{[-l|--ls]}}`

- Ուղարկեք հատուկ PostScript փաստաթուղթ ցանցի յուրաքանչյուր PostScript տպիչին.:

`ippfind --txt-pdl application/postscript {{[-x|--exec]}} ipptool -f {{path/to/document.ps}} '{}' print-job.test \;`

- Ուղարկեք PostScript թեստային փաստաթուղթ ցանցի յուրաքանչյուր PostScript տպիչին.:

`ippfind --txt-pdl application/postscript {{[-x|--exec]}} ipptool -f onepage-letter.ps '{}' print-job.test \;`

- Ուղարկեք PostScript փորձնական փաստաթուղթ ցանցի յուրաքանչյուր PostScript տպիչին, որի անունը համապատասխանում է `regex`-ին:

`ippfind --txt-pdl application/postscript {{[-h|--host]}} {{regex}} {{[-x|--exec]}} ipptool -f onepage-letter.ps '{}' print-job.test \;`
